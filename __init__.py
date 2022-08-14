from bs4 import BeautifulSoup
import pandas as pd


import re
import base64
import requests
from dataCleaning import clean_from_text
from example_payload import dict_to_payload, payload, split_payload_to_dict, headers
from formOptions import options

d = split_payload_to_dict(payload)

for k, v in options.items():
    d[k] = v


pld = dict_to_payload(d)
url = "https://staging.ke.com.pk:8490/index.aspx"
print()
response = requests.request("POST", url, headers=headers, data=pld, timeout=5)
c = clean_from_text(response)


for i in c:
    l = "  ".join(i)+"\n"
    print(l)
