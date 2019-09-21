#!/usr/bin/env python
from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.openconfig import bgp

sbx_iosxr_ao = {
    "address": "sbx-iosxr-mgmt.cisco.com",
    "port": 10000,
    "username": "admin",
    "protocol": "ssh",
}

if __name__ == "__main__":
    provider = NetconfServiceProvider(**sbx_iosxr_ao)
    crud = CRUDService()
    bgp = bgp.Bgp()
    bgp.global_.config.as_ = 65000
    crud.create(provider, bgp)
    provider.close()
