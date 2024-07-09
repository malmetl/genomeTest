import requests
from datetime import datetime


class GenomeHttpclient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        self.session.headers["Authorization"] = f"Bearer {token}"

    def get_authorization_request(self, data):
        auth_key = self.session.post(f'{self.base_url}/users/auth', json=data)
        if auth_key.status_code != 200:
            print(f"Error: {auth_key.status_code}, {auth_key.text}")

        return auth_key
