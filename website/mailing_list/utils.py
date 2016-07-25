import json
import re
import requests
from urllib2 import HTTPError

from mailmanclient import Client
from modularodm import Q

from framework.auth import User
from framework.auth.core import get_user
from framework.auth.signals import user_confirmed
from framework.celery_tasks import app
from framework.celery_tasks.handlers import queued_task
from framework.exceptions import HTTPError

from website import settings
from website.project.signals import contributor_added, contributor_removed, node_deleted
from website.notifications.utils import to_subscription_key

#from website.mailing_list.model import MailingListEventLog

###
# Initialize some resources/ ensure they exist.
#######

mailman_api_url = 'http://{}:{}/{}'.format(
    settings.MAILMAN_API_DOMAIN,
    settings.MAILMAN_API_PORT,
    settings.MAILMAN_API_VERSION
    )

mc = Client(
    mailman_api_url,
    settings.MAILMAN_API_USERNAME,
    settings.MAILMAN_API_PASSWORD
    )

# Ensure the domain that the mailing lists we will be creating should be on exists.
# If it does not, the create it.
if settings.OSF_MAILING_LIST_DOMAIN in map(lambda x: x.mail_host, mc.domains):    
    mail_domain = mc.get_domain(settings.OSF_MAILING_LIST_DOMAIN)
else:
    mail_domain = mc.create_domain(settings.OSF_MAILING_LIST_DOMAIN)


###############################################################################
# Define some tools to manipulate the mailman client
###############################################################################

class MailingListError():
    pass

def with_list_proxy(fn):
    def _fn(*args, **kwargs):
        @app.task
        def get_proxy(*args, **kwargs):
            try:
                kwargs['list_proxy'] = mc.get_list('{}@{}'.format(kwargs['list_mailbox'], settings.OSF_MAILING_LIST_DOMAIN))
            except:
                kwargs['list_proxy'] = mail_domain.create_list(kwargs['list_mailbox'])
            fn(*args, **kwargs)
        if kwargs.get('list_proxy'):
            fn(*args, **kwargs)
        else:
            get_proxy.apply_async(*args, **kwargs)
    return _fn

# If we call this, we need a mailing list. If it doesn't exist yet, we should 
# create it. If it does exist, we should ensure it is up to date.
# This calls out to another server, so we should not be block.
@app.task
@with_list_proxy 
def upsert_list(list_title=None, list_description=None, list_proxy=None, list_mailbox=None, contributors=None, public=False):
    #try:
    #    list_proxy = mc.get_list('{}@{}'.format(list_mailbox, settings.OSF_MAILING_LIST_DOMAIN))
    #except:
    #    list_proxy = mail_domain.create_list(list_mailbox)
    stt = list_proxy.settings
    stt[u'display_name'] = list_title
    stt[u'description'] = list_description
    stt[u'archive_policy'] = 'public' if public else 'private'
    #import ipdb; ipdb.set_trace()
    stt.save()
    contributors and add_contributors(list_proxy=list_proxy, contributors=contributors)

@user_confirmed.connect
def subscribe_on_confirm(user):
    for node in user.contributed:
        subscribe_contributor_to_mailing_list(node, user)

# Adds all of the emails associated with a user to a given mailing list.
# This calls out to another server, so we should not block.
# TODO: accept both user objects and guids as args.
@with_list_proxy
def add_contributor(list_mailbox=None, list_proxy=None, contributor=None):
    def not_subbed(email):
        try:
            list_proxy.get_member(email)
            return False
        except:
            return True
    to_sub = list(filter(not_subbed, contributor.emails))
    map(lambda email: list_proxy.subscribe(
        email,
        contributor.fullname,
        pre_verified = True,
        pre_confirmed = True
        ), to_sub)

def add_contributors(list_proxy=None, contributors=None):
    map(lambda contributor: add_contributor(list_proxy, contributor), contributors)

@contributor_added.connect
def contributor_added_handler(node, contributor, auth=None, throttle=None):
    add_contributor(list_mailbox=node._id, contributor=contributor)

@with_list_proxy
@app.task
def remove_contributor(list_proxy, contributor):
    def subbed(email):
        try:
            list_proxy.get_member(email)
            return True
        except:
            return False
    to_unsub = list(filter(subbed, contributor.emails))
    map(lambda email: list_proxy.unsubscribe(email))

@contributor_removed.connect
def contributor_removed_handler(node, contributor, auth=None, throttle=None):
    remove_contributor(node._id, contributor)

@with_list_proxy
def remove_contributors(list_proxy, contributors):
    map(lambda contributor: remove_contributor(list_proxy, contributor), contributors)



###############################################################################
# Decorator
###############################################################################

#def require_mailgun(func):
#    """ Execute MailGun API calls iff API key is set """
#    def wrapper(*args, **kwargs):
#        if settings.MAILGUN_API_KEY:
#            return func(*args, **kwargs)
#        return None
#    return wrapper

###############################################################################
# List Management Functions
###############################################################################

#@require_mailgun
#def get_info(node_id):
#    """ Returns information about the mailing list from Mailgun
#    :param str node_id: ID of the node in question
#    :returns dict info: mailing list info
#    """
#    return mc.get_list('{}@{}'.format(node_id, mail_domain.mail_domain))
#    resp = requests.get(
#        '{}/{}'.format(MAILGUN_BASE_LISTS_URL, address(node_id)),
#        auth=('api', settings.MAILGUN_API_KEY),
#    )
#    if resp.status_code == 200:
#        return resp.json()
#    elif resp.status_code == 404:
#        return None
#    raise HTTPError(resp.status_code, data={'message_long': resp.json() or ''})

#@require_mailgun
#def get_members(node_id):
#    """ Returns member list for mailing list from Mailgun
#    :param str node_id: ID of the node in question
#    :returns dict members: list of members
#    """
#    resp = requests.get(
#        '{}/{}/members'.format(MAILGUN_BASE_LISTS_URL, address(node_id)),
#        auth=('api', settings.MAILGUN_API_KEY),
#    )
#    if resp.status_code == 200:
#        return resp.json()
#    raise HTTPError(resp.status_code, data={'message_long': resp.json() or ''})

#@require_mailgun
def get_list(node_id):
    """ Returns information about the mailing list from Mailgun
    :param str node_id: ID of the node in question
    :returns: info, members: Two dictionaries about list and members
    """
    return mc.get_list('{}@{}'.format(node_id, settings.OSF_MAILMAN_DOMAIN))

#@require_mailgun
def create_list(node_id):
    """ Creates a new mailing list on Mailgun with all emails and subscriptions
    :param str node_id: ID of the node in question
    """
    #from website.models import Node  # avoid circular import
    #node = Node.load(node_id)
    
    #resp = requests.post(
    #    MAILGUN_BASE_LISTS_URL,
    #    auth=('api', settings.MAILGUN_API_KEY),
    #    data={
    #        'address': address(node_id),
    #        'name': list_title(node),
    #        'access_level': 'members'
    #    }
    #)
    #if resp.status_code != 200:
    #    raise HTTPError(resp.status_code, data={'message_long': resp.json() or ''})
    #
    #members_list = jsonify_users_list(node.contributors, unsubs=get_unsubscribes(node), initial=True)
    #mlist = md.create_list(node_id)
    #for m in members_list:
    #    mlist.subscribe(
    #            m,
    #            pre_verified = True,
    #            pre_confirmed = True
    #            )
    #update_multiple_users_in_list(node_id, members_list)
    #return mlist

#@require_mailgun
def delete_list(node_id):
    """ Deletes list on MailGun
    :param str node_id: ID of the node in question
    """
    #resp = requests.delete(
    #    '{}/{}'.format(MAILGUN_BASE_LISTS_URL, address(node_id)),
    #    auth=('api', settings.MAILGUN_API_KEY)
    #)
    #if resp.status_code not in [200, 404]:
    #    raise HTTPError(resp.status_code, data={'message_long': resp.json() or ''})

#@require_mailgun
def update_title(node_id):
    """ Updates the title of a mailing list to match the list's project
    :param str node_id: ID of the node in question
    """
    #from website.models import Node  # avoid circular import
    #node = Node.load(node_id)

    #resp = requests.put(
    #    '{}/{}'.format(MAILGUN_BASE_LISTS_URL, address(node_id)),
    #    auth=('api', settings.MAILGUN_API_KEY),
    #    data={
    #        'name': list_title(node)
    #    }
    #)
    #if resp.status_code != 200:
    #    raise HTTPError(resp.status_code, data={'message_long': resp.json() or ''})

#@require_mailgun
def update_single_user_in_list(node_id, user_id, email=None, enabled=True, old_email=None):
    """ Adds/updates single member of a mailing list on Mailgun
    Called to add, subscribe, or unsubscribe a user.

    :param str node: ID of node in question
    :param str user: ID of user to update
    :param str email: email address to add. If None, `user.username` assumed.
    :param bool enabled: Enable or disable user?
    :param str old_email: Previous email of this user in list, included when user changes primary email.
    """
    from website.models import Node, User  # avoid circular import
    node = Node.load(node_id)
    user = User.load(user_id)
    email = email or user.username

    if old_email:
        pass
    #    resp = requests.put(
    #        '{}/{}/members/{}'.format(MAILGUN_BASE_LISTS_URL, address(node_id), old_email),
    #        auth=('api', settings.MAILGUN_API_KEY),
    #        data={
    #            'subscribed': 'no',
    #            'vars': json.dumps({'_id': user_id, 'primary': False})
    #        }
    #    )
    #    if resp.status_code not in [200, 404]:
    #        raise HTTPError(resp.status_code, data={'message_long': resp.json() or ''})

    #resp = requests.post(
    #    '{}/{}/members'.format(MAILGUN_BASE_LISTS_URL, address(node._id)),
    #    auth=('api', settings.MAILGUN_API_KEY),
    #    data={
    #        'address': email,
    #        'subscribed': enabled and email == user.username and user not in get_unsubscribes(node),
    #        'vars': json.dumps({'_id': user._id, 'primary': email == user.username or bool(old_email)}),
    #        'upsert': True
    #    }
    #)
    #if resp.status_code != 200:
    #    raise HTTPError(resp.status_code, data={'message_long': resp.json() or ''})

#@require_mailgun
def remove_user_from_list(node_id, user_id):
    """ Removes single member of a mailing list on Mailgun
    Called when a contributor is removed from a Node.

    :param str node_id: ID of node in question
    :param str user_id: ID of user to remove
    """
    from website.models import User  # avoid circular import
    user = User.load(user_id)

    for email in user.emails:
        pass
    #    resp = requests.delete(
    #        '{}/{}/members/{}'.format(MAILGUN_BASE_LISTS_URL, address(node_id), email),
    #        auth=('api', settings.MAILGUN_API_KEY)
    #    )
    #    if resp.status_code not in [200, 404]:
    #        raise HTTPError(resp.status_code, data={'message_long': resp.json() or ''})

#@require_mailgun
def update_multiple_users_in_list(node_id, members):
    """ Adds/updates members of a mailing list on Mailgun

    :param str node_id: The id of the node in question
    :param list members: Paginated list of json-formatted user dicts to add/enable/update
    """
    for page in members:
        pass    
        #resp = requests.post(
        #    '{}/{}/members.json'.format(MAILGUN_BASE_LISTS_URL, address(node_id)),
        #    auth=('api', settings.MAILGUN_API_KEY),
        #    data={
        #        'upsert': True,
        #        'members': json.dumps(page)
        #    }
        #)
        #if resp.status_code != 200:
        #    raise HTTPError(resp.status_code, data={'message_long': resp.json() or ''})

#@require_mailgun
def full_update(node_id):
    """ Matches remote list with internal representation
    :param str node_id: The node to update the mailing list for
    """
    from website.models import Node, User  # avoid circular import
    node = Node.load(node_id)

    info, members = get_list(node_id)

    if node.is_deleted:
        delete_list(node_id)
    elif node.mailing_enabled:
        if 'list' in info:
            info = info['list']
            remote_subscribes = set([member['address'] for member in members['items'] if member['subscribed']])
            local_subscribes = set([user.username for user in get_recipients(node)])

            if info['name'] != list_title(node):
                # Update title if necessary
                update_title(node_id, node.title)

            if remote_subscribes != local_subscribes:
                # Push local changes
                members_list = jsonify_users_list(node.contributors, unsubs=get_unsubscribes(node))
                update_multiple_users_in_list(node_id, members_list)

            # Delete any noncontribs
            member_ids = set([member['vars']['_id'] for member in members['items'] if member.get('vars', {}).get('_id', False)])
            for u_id in member_ids:
                if u_id not in node.contributors:
                    user = User.load(u_id)
                    if user:
                        remove_user_from_list(node_id, u_id)

        else:
            create_list(node_id)
    else:
        if 'list' in info.keys():
            delete_list(node_id)


###############################################################################
# Celery Queued tasks
###############################################################################

@queued_task
@app.task(max_retries=3, default_retry_delay=3 * 60)  # Retry after 3 minutes
def celery_create_list(*args, **kwargs):
    create_list(*args, **kwargs)

@queued_task
@app.task(max_retries=3, default_retry_delay=3 * 60)  # Retry after 3 minutes
def celery_delete_list(*args, **kwargs):
    delete_list(*args, **kwargs)

@queued_task
@app.task(max_retries=3, default_retry_delay=3 * 60)  # Retry after 3 minutes
def celery_update_title(*args, **kwargs):
    update_title(*args, **kwargs)

@queued_task
@app.task(max_retries=3, default_retry_delay=3 * 60)  # Retry after 3 minutes
def celery_update_single_user_in_list(*args, **kwargs):
    update_single_user_in_list(*args, **kwargs)

@queued_task
@app.task(max_retries=3, default_retry_delay=3 * 60)  # Retry after 3 minutes
def celery_remove_user_from_list(*args, **kwargs):
    remove_user_from_list(*args, **kwargs)

@queued_task
@app.task(max_retries=3, default_retry_delay=3 * 60)  # Retry after 3 minutes
def celery_update_multiple_users_in_list(*args, **kwargs):
    update_multiple_users_in_list(*args, **kwargs)

@queued_task
@app.task(max_retries=3, default_retry_delay=3 * 60)  # Retry after 3 minutes
def celery_full_update(*args, **kwargs):
    full_update(*args, **kwargs)


###############################################################################
# Signalled Functions
###############################################################################

#@contributor_added.connect
#def subscribe_contributor_to_mailing_list(node, contributor, auth=None):
#    if contributor.is_active:
#        @app.task
#        def addContributor():
        
        #subscription = node.get_or_create_mailing_list_subscription()
        #subscription.add_user_to_subscription(contributor, 'email_transactional', save=True)
        #celery_update_single_user_in_list(node._id, contributor._id)
        #node.mailing_updated = True
        #node.save()




@node_deleted.connect
def remove_list_for_deleted_node(node):
    node.mailing_updated = True
    node.save()
    celery_delete_list(node._id)


###############################################################################
# Mailing List Helper Functions
###############################################################################

def jsonify_users_list(users, unsubs=(), initial=False):
    """ Serializes and paginates list of users for Mailgun

    :param list users: users to serialize
    :param list unsubs: unsubscribed users
    :param bool initial: whether or not to insert mailing_list_robot
    """
    members_list = []
    if initial:
        members_list.append({'address': address('mailing_list_robot'), 'subscribed': True})  # Routing robot

    for member in users:
        for email in member.emails:
            members_list.append({
                'address': email,
                'subscribed': member not in unsubs and email == member.username,
                'vars': {
                    '_id': member._id, 
                    'primary': email == member.username,
                    'name': member.full_name
                    }
            })

    # Mailgun allows 1000 user upserts per request
    return members_list
    #return [members_list[i:i + 999] for i in range(0, len(members_list), 999)]

def address(node_id):
    return '{}@{}'.format(node_id, settings.MAILGUN_LIST_ADDRESS_DOMAIN)

def list_title_pretty(node):
    return '{} Mailing List'.format(node.title)

def log_message(target, sender_email, message):
    """ Acquires and logs messages sent through Mailgun"""
    from website.models import Node  # avoid circular imports

    if target:
        node = Node.load(re.search(r'[a-z0-9]*@', target).group(0)[:-1])
    else:
        node = None

    sender = get_user(email=sender_email)

    # Create a log of this mailing event
    MailingListEventLog(
        email_content=message,
        destination_node=node,
        sending_user=sender,
    ).save()

def unsubscribe_user_hook(unsub, mailing_list):
    """ Hook triggered by MailGun when user unsubscribes.
    See `Unsubscribes Webhook` below https://documentation.mailgun.com/user_manual.html#tracking-unsubscribes
    for possible kwargs
    """
    from website.models import User, NotificationSubscription  # avoid circular imports
    user = User.find_one(Q('username', 'eq', unsub))
    node_id = mailing_list.split('@')[0]
    subscription = NotificationSubscription.load(to_subscription_key(node_id, 'mailing_list_events'))
    subscription.add_user_to_subscription(user, 'none', save=True)

def get_recipients(node):
    # Subscription options for mailing lists are 'transactional' and 'none'
    if node.mailing_enabled:
        from website.models import NotificationSubscription  # avoid circular import
        subscription = NotificationSubscription.load(to_subscription_key(node._id, 'mailing_list_events'))
        return subscription.email_transactional
    return []

def get_unsubscribes(node):
    # Non-subscribed users not guaranteed to be in subscription.none
    # Safer to calculate it
    if node.mailing_enabled:
        recipients = get_recipients(node)
        return [u for u in node.contributors if u not in recipients]
    return []
