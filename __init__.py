import pandas as pd


import requests
from dataCleaning import clean_from_text
from example_payload import PayloadProcessor, headers
from formOptions import FormOptions
from postTransformations import PostTransform


test= False
if test==True:
    with open("datadump.txt") as f:
        response = f.read()
else:
    processor=PayloadProcessor()
    d=processor.getdict()

    foption= FormOptions()
    formpartialoptions=foption.MoveToPage(9)
    processor.add_options_to_payload(formpartialoptions)
    pld=processor.getPayload()
    url = "https://staging.ke.com.pk:8490/index.aspx"

    response = requests.request("POST", url, headers=headers, data=pld, timeout=5)
    response=response.text


c = clean_from_text(response)
pt= PostTransform(c)
pt.to_csv("test.csv")    
    