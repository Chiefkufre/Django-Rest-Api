from email import message
import requests


endpoint = 'http://127.0.0.1:8080/api/products/6'


data = {'title': 'clothe-men', 'content':'Uk-made', 'price': 23}

get_response = requests.get(endpoint, json=data)

print(get_response.json())
