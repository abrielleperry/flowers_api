#!/usr/bin/python3
''' create api for flower list '''
import requests

URL = "https://perenual.com/api/species-list?key=sk-DEwc66044f446830c4882"

payload = {}
headers = {}

response = requests.request("GET", URL, headers=headers, data=payload, timeout=5)

print(response.text)
