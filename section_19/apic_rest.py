#!/usr/bin/env python

import requests
import json
from pprint import pprint

# disable warnings, set verify=Flase in requests due to lab self-signed certs
# in a production environment should have proper certificates
requests.packages.urllib3.disable_warnings()


def apic_login(apic_url, username, password):
    url = apic_url + "/api/aaaLogin.json"
    auth = {"aaaUser": {"attributes": {"name": username, "pwd": password}}}
    authenticate = requests.post(url, data=json.dumps(auth), verify=False)
    return authenticate.cookies


def get_subnets(apic_url, cookies):
    uri = "/api/class/fvSubnet.json"
    url = apic_url + uri
    req = requests.get(url, cookies=cookies, verify=False)
    response = req.text
    return response


def get_tenant_fvAEPg(apic_url, tenant, cookies):
    uri = (
        f"/api/node/mo/uni/tn-{tenant}.json?"
        "query-target=subtree&target-subtree-class=fvAEPg"
    )
    url = apic_url + uri
    req = requests.get(url, cookies=cookies, verify=False)
    response = req.text
    return response


if __name__ == "__main__":

    apic_sbx_ao = {
        "apic_url": "https://sandboxapicdc.cisco.com",
        "username": "admin",
        "password": "ciscopsdt",
    }
    cookies = apic_login(**apic_sbx_ao)

    # Get all subnet data
    rsp = get_subnets(apic_sbx_ao["apic_url"], cookies)
    rsp_dict = json.loads(rsp)
    subnets = rsp_dict["imdata"]
    for subnet in subnets:
        print(f"Name: {subnet['fvSubnet']['attributes']['name']}")
        print(f"IP: {subnet['fvSubnet']['attributes']['ip']}")
        print(f"dn: {subnet['fvSubnet']['attributes']['dn']}")
        print("\n", "-" * 80, "\n")

    # query filter
    tenant = "Heroes"
    rsp = get_tenant_fvAEPg(apic_sbx_ao["apic_url"], tenant, cookies)
    rsp_dict = json.loads(rsp)
    tenant_epg = rsp_dict["imdata"]
    pprint(tenant_epg)
