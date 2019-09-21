#!/usr/bin/env python
import requests
import json

requests.packages.urllib3.disable_warnings()

base_url = "https://sandboxapicem.cisco.com:443/api/v1"

url = base_url + "/ticket"

headers = {"content-type": "application/json"}
payload_dict = {"username": "devnetuser", "password": "Cisco123!"}
payload_json = json.dumps(payload_dict)

response = requests.post(url, data=payload_json, headers=headers, verify=False)

response_dict = json.loads(response.text)

# should have error checking around this
headers["x-auth-token"] = response_dict["response"]["serviceTicket"]

url = base_url + "/policy"
response = requests.get(url, headers=headers, verify=False)

response_dict = json.loads(response.text)
print(json.dumps(response_dict, indent=4))
