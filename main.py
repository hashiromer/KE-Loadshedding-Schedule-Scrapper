import pandas as pd


import requests
from dataCleaning import clean_from_text
from example_payload import headers
from formOptions import FormOptions
from postTransformations import PostTransform


class Main:
    def __init__(self, isTest=False):
        self.test=isTest

    def run(self):
        if self.test==True:
            with open("datadump.txt") as f:
                response = f.read()
        else:

            foption= FormOptions()
            # foption.moveBlock()
            encodedPayload=foption.getPayload()
            url = "https://staging.ke.com.pk:8490/index.aspx"
            response = requests.request("POST", url, headers=headers, data=encodedPayload, timeout=5)
            response=response.text


        c = clean_from_text(response)
        pt= PostTransform(c)
        pt.to_csv("test.csv")    
            