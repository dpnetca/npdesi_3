#!/usr/bin/env python
from ncclient import manager
from lxml import etree

gns3_CSR1 = {
    "host": "192.168.122.203",
    "port": 830,
    "username": "admin",
    "password": "cisco",
    "hostkey_verify": False,
    "allow_agent": False,
    "look_for_keys": False,
    "device_params": {"name": "csr"},
}

if __name__ == "__main__":
    with manager.connect(**gns3_CSR1) as device:
        get_filter = """
            <native xmlns = "http://cisco.com/ns/yang/ned/ios">
              <interface>
                <GigabitEthernet>
                  <name>1</name>
                </GigabitEthernet>
              </interface>
            </native>
        """

        # nc_get_reply = device.get(("subtree", get_filter))
        nc_get_reply = device.get()
        print(etree.tostring(nc_get_reply.data_ele, pretty_print=True))
