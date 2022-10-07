from email import message
import requests


# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://127.0.0.1:8080/api/'

get_response = requests.post(endpoint, json={'my_discount': 20, 'title': 'clothe-men', 'content':'Uk-made', 'price': 23})

print(get_response.json())
