import httpx
import requests

requests.get('https://gmail.com', timeout=30, verify=True)
requests.get('https://gmail.com', timeout=30, verify=False)
requests.post('https://gmail.com', timeout=30, verify=True)
requests.post('https://gmail.com', timeout=30, verify=False)
requests.put('https://gmail.com', timeout=30, verify=True)
requests.put('https://gmail.com', timeout=30, verify=False)
requests.delete('https://gmail.com', timeout=30, verify=True)
requests.delete('https://gmail.com', timeout=30, verify=False)
requests.patch('https://gmail.com', timeout=30, verify=True)
requests.patch('https://gmail.com', timeout=30, verify=False)
requests.options('https://gmail.com', timeout=30, verify=True)
requests.options('https://gmail.com', timeout=30, verify=False)
requests.head('https://gmail.com', timeout=30, verify=True)
requests.head('https://gmail.com', timeout=30, verify=False)