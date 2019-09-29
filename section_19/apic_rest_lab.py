#!/usr/bin/env python
import requests
import json

# disable warnings, set verify=Flase in requests due to lab self-signed certs
# in a production environment should have proper certificates
requests.packages.urllib3.disable_warnings()


def apic_login(apic_url, username, password):
    url = apic_url + "/api/aaaLogin.json"
    auth = {"aaaUser": {"attributes": {"name": username, "pwd": password}}}
    authenticate = requests.post(url, data=json.dumps(auth), verify=False)
    return authenticate.cookies


def add_tenant(apic_url, tenant_data, cookies):
    uri = "/api/node/mo/uni.json"
    url = apic_url + uri
    data = json.dumps(tenant_data)
    result = requests.post(url, cookies=cookies, data=data, verify=False)
    print(result.status_code)
    print(result.text)


def add_vrf(apic_url, tenant, vrf_data, cookies):
    uri = f"/api/node/mo/uni/{tenant}.json"
    url = apic_url + uri
    result = requests.post(
        url, cookies=cookies, data=json.dumps(vrf_data), verify=False
    )
    print(result.status_code)
    print(result.text)


def get_tenants(apic_url, cookies):
    uri = "/api/class/fvTenant.json"
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

    tenant_data = {
        "fvTenant": {
            "attributes": {
                "dn": "uni/tn-Procurement",
                "name": "Procurement",
                "rn": "tn-Procurement",
                "status": "created,modified",
            },
            "children": [],
        }
    }

    add_tenant(apic_sbx_ao["apic_url"], tenant_data, cookies)

    vrf_data = {
        "fvCtx": {
            "attributes": {
                "dn": "uni/tn-Procurement/ctx-Internal",
                "name": "Internal",
                "rn": "ctx-Internal",
                "status": "created",
            },
            "children": [],
        }
    }
    add_vrf(apic_sbx_ao["apic_url"], "tn-Procurement", vrf_data, cookies)

    rsp = get_tenants(apic_sbx_ao["apic_url"], cookies)
    rsp_dict = json.loads(rsp)
    tenants = rsp_dict["imdata"]

    for tenant in tenants:
        print(tenant["fvTenant"]["attributes"]["name"])
