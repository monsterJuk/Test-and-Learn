from config import API_KEY, API_SECRET
import requests

base_url = 'https://contract.mexc.com/'
endpoints = {
    'server_time': 'api/v1/contract/ping',
    'info': 'api/v1/private/account/assets'
}

url = base_url + endpoints.get('info')
headers = {'ApiKey': API_KEY}

response = requests.get(url=url, headers=headers)
print(response.json())
