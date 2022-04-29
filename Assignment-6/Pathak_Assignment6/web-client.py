import requests
import json

url = "http://127.0.0.1:5000/name"

payload = {'data': "hand1.png"}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.text, response.status_code)
