#!/usr/bin/env python
import requests

# Ignore warnings about inscure https certificates
requests.packages.urllib3.disable_warnings()

device_ip = "192.168.122.203"

if __name__ == "__main__":
    auth = requests.auth.HTTPBasicAuth("admin", "cisco")
    # headers = {"Accept": "application/vnd.yang.data+json"}
    headers = {"Accept": "application/yang-data+json"}
    # base_url = f"https://{device_ip}/restconf/api/config/native"
    base_url = f"https://{device_ip}/restconf/data/Cisco-IOS-XE-native:native/"
    url = base_url + "/ip/route"
    response = requests.get(url, verify=False, headers=headers, auth=auth)
    # print(response.status_code)
    print(response.text)
