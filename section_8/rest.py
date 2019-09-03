#!/usr/bin/env python

import requests

# import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    device = "10.10.10.10"
    auth = HTTPBasicAuth("cisco", "cisco")
    headers = {"Accept": "application/json"}
    url = f"http://{device}/api/config/interfaces"
    response = requests.get(url, verify=False, headers=headers, auth=auth)
    print(response.status_code)
    print(response.text)
