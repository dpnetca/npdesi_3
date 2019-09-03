#!/usr/bin/env python

import json

if __name__ == "__main__":
    facts = {"hostname": "nxosv", "os": "7.3", "location": "San_Jose"}
    # print facts dictionary
    print(facts)
    # print facts as a JSON string
    print(json.dumps(facts, indent=4))
    # print a specific value of key
    print(facts["os"])

    print("\n")
    print("*" * 20)
    print("\n")

    facts = '{"hostname": "nxosv", "os": "7.3", "location": "San_Jose"}'
    print(facts)
    print(type(facts))
    # print facts['os']
    # TypeError: string indices must be integers, not str
    factsd = json.loads(facts)
    print(json.dumps(factsd, indent=4))
