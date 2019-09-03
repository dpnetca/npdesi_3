#!/usr/bin/env python

from ncclient import manager
from lxml import etree


# seperated out connection parameters
sbx_csr_ao = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "port": 10000,
    "username": "developer",
    "password": "C1sco12345",
    "hostkey_verify": False,
    "allow_agent": False,
    "look_for_keys": False,
    "device_params": {"name": "csr"},
}

with manager.connect(**sbx_csr_ao) as device:
    # changed xmlns  from "http://cisco.com/ns/yang/ned/ios">
    get_filter = """
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
         <interface>
         </interface>
        </native>
    """
    nc_get_reply = device.get(("subtree", get_filter))
    reply = etree.tostring(nc_get_reply.data_ele, pretty_print=True)
    # Added stgeps to decode byte string as utf-8 for formatting
    print(reply.decode("utf-8"))
