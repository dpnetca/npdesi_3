#!/usr/bin/env python

from ncclient import manager

# from lxml import etree
# from lxml.builder import ElementMaker


# sbx_nxos_ao = {
#     "host": "sbx-nxos-mgmt.cisco.com",
#     "port": 10000,
#     "username": "admin",
#     "password": "Admin_1234!",
#     "hostkey_verify": False,
#     "allow_agent": False,
#     "look_for_keys": False,
#     "device_params": {"name": "nexus"},
# }

gns3_nxosv1 = {
    "host": "192.168.122.202",
    "port": 22,
    "username": "admin",
    "password": "cisco",
    "hostkey_verify": False,
    "allow_agent": False,
    "look_for_keys": False,
    "device_params": {"name": "nexus"},
}

get_filter = """
            <show>
                <hostname>
                </hostname>
            </show>
            """

# E = ElementMaker()
# nc_filter = E.show(E.hostname())

with manager.connect(**gns3_nxosv1) as device:
    nc_get_reply = device.get(("subtree", get_filter))
    # nc_get_reply = device.get(("subtree", nc_filter))

print(nc_get_reply.xml)

ns_map = {"mod": "http://www.cisco.com/nxos:1.0:vdc_mgr"}
xml_rsp = nc_get_reply.data_ele.find(".//mod:hostname", ns_map)
print("\n")
print("#" * 20)
print("\n")
value = xml_rsp.text
print(value)
