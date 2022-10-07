from email import message
import requests


endpoint = 'http://127.0.0.1:8080/api/products/6'

get_response = requests.get(endpoint, json={'my_discount': 20, 'title': 'clothe-men', 'content':'Uk-made', 'price': 23})

print(get_response.json())
