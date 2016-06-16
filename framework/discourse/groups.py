
class NodeGroupProxy:

    def __init__(self, node):
        self.project_node_id = 

    def resolve(self):
        response = requests.post(f.url, data={
            'api_key': settings.DISCOURSE_API_KEY
            'api_username': settings.DISCOURSE_API_ADMIN_USER
            'name': self.project_node_id,
            'visible': 'true' if parent.is_public else 'false'
            'alias_level': '3'
            })
        if response.status_code != 200:
            raise HttpException('Expected reponse code 200, got {}'.format(response.status_code))
            return response

        return response

    def debrief_node():
        pass

