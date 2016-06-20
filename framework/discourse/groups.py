import requests
from furl import furl

from website import settings
from . import utils
from .exceptions import *

class NodeGroupProxy:

    def __init__(self, node, topic=None):
        self.node = node
        self.topic = topic
        self.contributors = node.contributors
        self.project_node = node if node.target_type in ['wikis', 'files'] else getattr(node, 'node', node)
        self.group_name = node.discussion.get('group_name', node._id)
        self.group_id = node.discussion.get('group_id')
        import ipdb; ipdb.set_trace()
        if self.group_id: return
        self.resolve()
        self.add_users()

    def resolve(self):
        f = furl(settings.DISCOURSE_SERVER_URL).join('/admin/groups')
        response = requests.post(f.url, data={
            'api_key': settings.DISCOURSE_API_KEY,
            'api_username': settings.DISCOURSE_API_ADMIN_USER,
            'name': self.group_name,
            'visible': 'true' if self.topic else 'false',
            'alias_level': '3'
            })
        if response.status_code != 200:
            raise RequestError('Expected reponse code 200, got {}'.format(response.status_code))
        r = response.json()
        self.group_id = r[u'basic_group'][u'id']
        self.debrief()
        return

    def add_users(self):
        # adding users to a group has to be a separate request for discourse
        f = furl(settings.DISCOURSE_SERVER_URL)
        f.path.segments = [
            'admin',
            'groups',
            str(self.group_id),
            'owners.json'
            ]
        response = requests.put(f.url, data={
            'api_key': settings.DISCOURSE_API_KEY,
            'api_username': settings.DISCOURSE_API_ADMIN_USER,
            'group_id': self.group_id,
            'usernames': ','.join(map(lambda c: c._id, self.contributors))
            })
        if response.status_code != 200:
            self.add_users()
            raise RequestError('Expected reponse code 200, got {}'.format(response.status_code))
        r = response.json()
        self.debrief()
        return
    
    def delete(self):
        pass

    def debrief(self):
        if self.project_node:
            self.node.discussion['group_id'] = self.group_id
            self.node.discussion['group_name'] = self.group_name
            self.node.save()
        if self.topic:
            self.topic.group_id = self.group_id

###############################################################################
