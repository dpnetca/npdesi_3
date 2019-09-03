#!/usr/bin/env python

import requests
import json
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = "https://sbx-nxos-mgmt.cisco.com/ins"
    auth = HTTPBasicAuth("admin", "Admin_1234!")

    headers = {"Content-Type": "application/json"}
    payload = {
        "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "1",
            "input": "show version",
            "output_format": "json",
        }
    }

    response = requests.post(
        url, verify=False, data=json.dumps(payload), headers=headers, auth=auth
    )

    print("Status Code: " + str(response.status_code))
    rx_object = json.loads(response.text)
    print(json.dumps(rx_object, indent=4))
