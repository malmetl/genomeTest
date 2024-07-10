from genomeTest import GenomeHttpclient
from datetime import datetime
import json
import urllib3

client = GenomeHttpclient("https://genomepre.crie.ru",
                          token="")


def test_auth():
    data = {
        'username': "crie_kurochkin",
        'password': "2CZSudsG",
    }
    auth_key = client.get_authorization_request(data=data)
    print(auth_key.text)
    assert auth_key.status_code == 200

def test_auth_negative():
    data = {
        'username': "crie_kurochkin",
        'password': "2CZSudsG",
    }
    auth_key = client.get_authorization_request(data=data)
    assert auth_key.status_code != 400