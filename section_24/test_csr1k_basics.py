#!/usr/bin/env python

import unittest
import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()


class TestDevieConfiguration(unittest.TestCase):
    def csr_get(self, uri):
        requests.packages.urllib3.disable_warnings()
        base_url = "https://192.168.122.203"
        auth = HTTPBasicAuth("admin", "cisco")
        url = base_url + uri
        headers = {"Accept": "application/yang-data+json"}
        response = requests.get(url, verify=False, headers=headers, auth=auth)
        return response

    def test_npdesi_snmp_ro(self):
        """Validate npdesi is a configured RO string
        """
        uri = "/restconf/data/Cisco-IOS-XE-native:native/snmp-server/community"
        response = self.csr_get(uri)
        parse = json.loads(response.text)
        community_list = parse["Cisco-IOS-XE-snmp:community"]
        expected = {"name": "npdesi", "access-list-name": "ro"}
        is_there = expected in community_list
        self.assertTrue(is_there)

    def test_cisco_snmp_ro(self):
        """Validate cisco is a configured RO string
        """
        uri = "/restconf/data/Cisco-IOS-XE-native:native/snmp-server/community"
        response = self.csr_get(uri)
        parse = json.loads(response.text)
        community_list = parse["Cisco-IOS-XE-snmp:community"]

        expected = {"name": "cisco", "access-list-name": "ro"}
        is_there = expected in community_list
        self.assertTrue(is_there)

    def test_cisco_secure_snmp_rw(self):
        """Validate cisco_secure is a configured RW string
        """
        uri = "/restconf/data/Cisco-IOS-XE-native:native/snmp-server/community"
        response = self.csr_get(uri)
        parse = json.loads(response.text)
        community_list = parse["Cisco-IOS-XE-snmp:community"]

        expected = {"name": "cisco_secure", "access-list-name": "rw"}
        is_there = expected in community_list
        self.assertTrue(is_there)

    def test_devops_user(self):
        """Validate devops user exists
        """
        uri = "/restconf/data/Cisco-IOS-XE-native:native/username"
        response = self.csr_get(uri)
        parse = json.loads(response.text)
        user_list = parse["Cisco-IOS-XE-native:username"]
        is_there = any(user["name"] == "devops" for user in user_list)
        self.assertTrue(is_there)


if __name__ == "__main__":
    unittest.main()
