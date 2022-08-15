from ast import While
import pandas as pd


import requests
from dataCleaning import clean_from_text
from example_payload import headers
from formOptions import PayloadManager
from postTransformations import PostTransform


class Main:
    def __init__(self, isTest=False):
        self.test=isTest

    def run(self):
        if self.test==True:
            with open("datadump.txt") as f:
                response = f.read()
        else:
            col=[
                'Grids',
                'Feeder_Name',
                'Group',
                'Category',
                '1st_Cycle',
                '2nd_Cycle',
                '3rd_Cycle',
                '4th_Cycle',
                '5th_Cycle',
                '6th_Cycle',
            ]
            df=pd.DataFrame(columns=col)

            payload_manager= PayloadManager()
            count=0

            while True:
                print(count)
                count+=1
                block=payload_manager.getBlock()

                if block ==7:
                    df.to_csv("data.csv", index=False)
                    break
                encodedPayload=payload_manager.getEncodedPayload()
                url = "https://staging.ke.com.pk:8490/index.aspx"
                response = requests.request(
                    "POST", url, headers=headers, data=encodedPayload, timeout=5)
                response=response.text



                c = clean_from_text(response)
                pt= PostTransform(c)

                data=pd.DataFrame(pt.get_data(), columns=col)

                df=df.append(data, ignore_index=True)
                if df.duplicated().sum()>0:
                    print("Duplicates found")
                    df=df.drop_duplicates()
                    payload_manager.moveBlock()
                else:
                    payload_manager.moveCursortoNextPage()
                   
               
        
       
       
            