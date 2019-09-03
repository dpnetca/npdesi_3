#!/usr/bin/env python
import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()

asa_ip = "192.168.122.201"
url = f"https://{asa_ip}/api/monitoring/device/components/version"
auth = HTTPBasicAuth("admin", "cisco")

response = requests.get(url, verify=False, auth=auth)

if response.status_code == 200:
    print("Status Code: " + str(response.status_code))
    parse = json.loads(response.text)
    print(json.dumps(parse, indent=4))
else:
    print("ERROR Code: " + str(response.status_code))
