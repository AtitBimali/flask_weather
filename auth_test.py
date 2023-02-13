import requests

url = 'http://localhost:5000/register'
data = {'username': '<your_username>', 'password': '<your_password>'}

response = requests.post(url, data=data)
print(response.json())
