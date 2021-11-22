import requests
import json

response = requests.post("http://localhost:9966/api/auth/login",
                         headers={'X-Requested-With': 'XMLHttpRequest'},
                         json={"username": "matthews", "password": ""})
response = response.json()
token = response['token']