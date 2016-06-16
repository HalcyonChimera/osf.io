import re
from furl import furl
import requests

from website import settings
from . import utils
import time

###############################################################################

admin = settings.DISCOURSE_API_ADMIN_USER
api_key = settings.DISCOURSE_API_KEY

###############################################################################

class CommunicationError(Exception):
    pass

class NodeTopicProxy:

    server_url = settings.DISCOURSE_SERVER_URL

    # This should be refactored for a default and when the 
    # node does have a discussion attribute
    def __init__(self, node=default_node):
        self.context_node = node
        self.guid = node._id
        self.category = node.category
        if node.target_type == 'nodes':
            self.node_type = node.project_or_component
            self.title = node.title
        if node.target_type == 'wikis':
            self.node_type = 'wiki'
            self.title = node.page_name
        if node.target_type == 'files':
            self.node_type = 'file'
            self.title = node.name
        self.description = re.compile(r'([\\`*_{}[\]()#.!-])').sub(r'\\\1', self.title)
        self.topic_privacy = 'private_message' # projects are private by default
        self.is_deleted = node.is_deleted
        # If we want access to the discourse topic, we're wanting it to exist.
        # If we dont have a discussion attribute on the node, we can't access it,
        # so we'll need to create it.
        if not node.discussion:
            self.url = furl(settings.DOMAIN).join(node.get_persistant_guid()._id).url
            self.post_id = None
            self.post()
        else:
            # This should be an error if not?
            self.post_id = node.discussion.post_id
        return 

    # Let's raise an exception if we try and call methods on an instance
    # after it's deleted.
    def disable_after_deletion(func):
        def wrapped(self, *args, **kwargs):
            if self.is_deleted:
                raise CommunicationError('This topic has been deleted.')
            func(self, *args, **kwargs)
        return wrapped

    @disable_after_deletion
    def debrief_node(self):
        self.node.discussion = {
            'topic_id': self.topic_id,
            'group_id': self.group_id,
            'post_id': self.post_id
            }

    @disable_after_deletion
    def post(self, tries=3):
        f = furl(settings.DISCOURSE_SERVER_URL).join('/posts')
        if self.post_id != None:
            f.join(self.post_id)
        response = requests.post(f.url, json={
            'raw': "\n".join([
                '`'+self.title+'``'+self.url+'`',
                'Contributors: '+', '.join(map(lambda c: c.display_full_name(), self.contributors)),
                'Date Created: ' + self.date_created.strftime('%Y-%m-%d %H:%M:%S'),
                'Category: '+self.category,
                'Description: '+self.description,
                'License: '+self.license
                ]),
            'category': '',
            'is_warning': 'false',
            'title': self.guid,
            'tags[]': self.tags,
            'archetype': self.topic_privacy,
            'target_usernames': ','.join(map(lambda c: c._id, node.contributors)),
            'api_username': settings.DISCOURSE_API_ADMIN_USER,
            'api_key': settings.DISCOURSE_API_KEY
            })
        if response.status_code == 200:
            self.debrief_node()
            return response
        return response

    @disable_after_deletion
    def delete(self):
        if not self.topic_id:
            raise AttributeError('Cannot delete a discourse topic without a discourse topic id.')
        f = furl(settings.DISCOURSE_SERVER_URL).join('/t')
        f.join(self.topic_id)
        requests.delete(f.url)
        self.context_node.discourse = None
        self.deleted = true
        
###############################################################################
