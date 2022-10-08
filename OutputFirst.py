#!/usr/bin/env python
# coding: utf-8

import json
import requests

url = "https://api.github.com/repos/MNYudina/Seminars/stargazers"
response = requests.get(url)

print(json.dumps(response.json()[0], indent=1))
print()

for (k,v) in response.headers.items():
 print(k, "=>", v)
