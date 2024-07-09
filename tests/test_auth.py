from genomeTest import GenomeHttpclient
from datetime import datetime
import json
client = GenomeHttpclient("https://genomepre.crie.ru",
                          token="b8a58b7999ae944f3bd1fd1781442fb14433504ff6fd648493c4d0c780514944")


def test_auth():
    data = {
        'username': "crie_kurochkin",
        'password': "2CZSudsG",
    }
    auth_key = client.get_authorization_request(data=data)
    assert auth_key.status_code == 200

def test_auth_negative():
    data = {
        'username': "crie_kurochkin",
        'password': "2CZSudsG",
    }
    auth_key = client.get_authorization_request(data=data)
    assert auth_key.status_code != 400