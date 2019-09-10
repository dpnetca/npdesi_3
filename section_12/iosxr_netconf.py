#!/usr/bin/env python
from ncclient import manager

# from lxml import etree

sbx_iosxr_ao = {
    "host": "sbx-iosxr-mgmt.cisco.com",
    "port": 10000,
    "username": "admin",
    "password": "C1sco12345",
    "hostkey_verify": False,
    "allow_agent": False,
    "look_for_keys": False,
    "device_params": {"name": "iosxr"},
}

if __name__ == "__main__":
    with manager.connect(**sbx_iosxr_ao) as device:
        nc_filter = """
            <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
              <interface-configuration>
                <interface-name>MgmtEth0/0/CPU0/0</interface-name>
              </interface-configuration>
            </interface-configurations>
        """

        nc_get_reply = device.get(("subtree", nc_filter))
        print(nc_get_reply)

        nc_filter = """
            <config>
            <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
            <interface-configuration>
                <active>act</active>
                <interface-name>Loopback123</interface-name>
                <interface-virtual/>
            </interface-configuration>
            </interface-configurations>
            </config>
        """
        nc_reply = device.edit_config(target="candidate", config=nc_filter)
        device.commit()
        print(nc_reply)
