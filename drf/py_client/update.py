from email import message
import requests


endpoint = 'http://127.0.0.1:8080/api/products/6/delete'

data = {
    'title': 'Popular clothings', 
    'content':'Uk-made', 
    'price': 23}

get_response = requests.delete(endpoint)

print(get_response.json())
