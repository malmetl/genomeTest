import requests
from datetime import datetime


class GenomeHttpclient:
    def __init__(self, base_url, token, pathogen_type_id='29'):
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"
        self.pathogen_type_id = pathogen_type_id

    def get_authorization_request(self, data):
        auth_key = self.session.post(f'{self.base_url}/users/auth', json=data)
        if auth_key.status_code != 200:
            print(f"Error: {auth_key.status_code}, {auth_key.text}")

        return auth_key

    def post_package_request(self, data):
        new_sample_request = self.session.post(f'{self.base_url}/api/v1/import/package', json=data)
        if new_sample_request.status_code != 200:
            print(f"Error: {new_sample_request.status_code}, {new_sample_request.text}")
            return new_sample_request
