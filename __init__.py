import pandas as pd


import requests
from dataCleaning import clean_from_text
from example_payload import dict_to_payload, payload, split_payload_to_dict, headers
from formOptions import FormOptions
from postTransformations import PostTransform

df=pd.DataFrame()
d = split_payload_to_dict(payload)
foption= FormOptions()
# foption.moveBlock()
f=foption.MoveToPage(1)

# foption=formOptions.moveCursortoNextPage()
# foption=formOptions.moveCursortoNextPage()



for k, v in f.items():
    d[k] = v


pld = dict_to_payload(d)
url = "https://staging.ke.com.pk:8490/index.aspx"
print()


test= True
if test==True:
    with open("datadump.txt") as f:
        response = f.read()
else:
    response = requests.request("POST", url, headers=headers, data=pld, timeout=5)
    response=response.text

c = clean_from_text(response)
pt= PostTransform(c)
pt.to_csv("test.csv")    
    