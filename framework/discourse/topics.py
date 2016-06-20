import re
from furl import furl
import requests

from website import settings
from . import groups
from . import errors
from . import utils
from .exceptions import *
import time

class Description(object):

    def __init__(self, ctx):
        self.ctx = ctx
        self.overridden = False
    def __set__(self, value):
        self.overriden = True
        self.value = value
    def __get__(self):
        return self.value if self.overridden else compose_description(self)

class NodeTopicProxy:

    server_url = settings.DISCOURSE_SERVER_URL

    # This should be refactored for a default and when the 
    # node does have a discussion attribute
    def __init__(self, node):
        self.node = node
        if node.target_type == 'nodes':
            self.type = node.project_or_component
            self.title = node.title
        if node.target_type == 'wikis':
            self.type = 'wiki'
            self.title = node.page_name
        if node.target_type == 'files':
            self.type = 'file'
            self.title = node.name
        self.guid = node._id
        self.category = node.category
        self.date_created = node.date_created
        self.contributors = node.contributors
        self.description = node.description
        self.is_deleted = node.is_deleted
        self.license = node.license if node.license != None else u''
        self.tags = [self.guid]
        self.group_proxy = groups.NodeGroupProxy(node, topic=self)
        # If we want access to the discourse topic, we're wanting it to exist.
        # If we dont have a discussion attribute on the node, we can't access it,
        # so we'll need to create it.
            # This should be an error if not?
        self.topic_id = node.discussion.get('topic_id', None)
        self.post_id = node.discussion.get('post_id', None)
        if self.topic_id and self.post_id:
            return 
        self.topic_privacy = 'private_message' # projects are private by default
        self.url = furl(settings.DOMAIN).join(self.guid).url
        self.resolve()

    # Let's raise an exception if we try and call methods on an instance
    # after it's deleted.
    def disable_after_deletion(func):
        def wrapped(self, *args, **kwargs):
            if self.is_deleted:
                raise CommunicationError('This topic has been deleted.')
            func(self, *args, **kwargs)
        return wrapped

    @disable_after_deletion
    def resolve(self, tries=3):
        f = furl(settings.DISCOURSE_SERVER_URL)
        f.path.segments.append('posts')
        if self.post_id != None:
            f.path.segments.append(str(self.post_id))
        users = map(lambda c: c._id, self.contributors)
        users.append(str(self.group_id))
        import ipdb; ipdb.set_trace()
        response = requests.post(f.url, data={
            'raw': self.create_description(), 
            'category': '',
            'is_warning': 'false',
            'title': self.guid,
            'tags[]': self.tags,
            'archetype': self.topic_privacy,
            'target_usernames': ','.join(users),
            'api_username': settings.DISCOURSE_API_ADMIN_USER,
            'api_key': settings.DISCOURSE_API_KEY
            })
        if response.status_code == 200:
            r = response.json()
            self.topic_id = r[u'topic_id']
            self.post_id = r[u'id']
            self.debrief_node()
            return response
        self.resolve()
        #raise RequestError('not 200, it was {}'.format(response.status_code))

    @disable_after_deletion
    def delete(self):
        if not self.topic_id:
            raise AttributeError('Cannot delete a discourse topic without a discourse topic id.')
        f = furl(settings.DISCOURSE_SERVER_URL).join('/t')
        f.join(self.topic_id)
        requests.delete(f.url)
        self.context_node.discourse = None
        self.deleted = true

    @disable_after_deletion
    def debrief_node(self):
        self.node.discussion['topic_id'] = self.topic_id,
        self.node.discussion['post_id'] = self.post_id
        self.node.save()
    
    def create_description(self):
        return "\n".join([
            '`'+self.title+'``'+self.url+'`',
            'Contributors: '+', '.join(map(lambda c: c.display_full_name(), self.contributors)),
            'Date Created: ' + self.date_created.strftime('%Y-%m-%d %H:%M:%S'),
            'Category: '+self.category,
            'Description: '+self.description,
            'License: '+self.license
            ])

###############################################################################
