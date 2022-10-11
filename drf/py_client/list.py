from email import header
import requests
from getpass import getpass
from gettext import gettext


auth_endpoint = 'http://127.0.0.1:8080/api/auth/'

password = getpass()
username = gettext('cfe')

data = {
    'password': password,
    'username': username
}

auth_response = requests.post(auth_endpoint, json=data)

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = 'http://127.0.0.1/api/products/'

    header = {
        'Authorization': f"Bearer {token}"
    }

    get_response = requests.get(endpoint, headers=header)

    print(get_response.json())

