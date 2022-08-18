import pandas as pd
import requests
from DataRow import DataRow
from example_payload import headers
from formOptions import PayloadManager
from postTransformations import PostTransform
import time


class Main:
    def __init__(self, isTest=False):
        self.test=isTest

    def run(self):
        if self.test==True:
            with open("datadump.txt") as f:
                response = f.read()
        else:
            rows=set()
            payload_manager= PayloadManager()
            count=0

            while True:
                print(count)
                count+=1
                block=payload_manager.getBlock()

                if block ==7:
                    print("Done: Existing")
                    #Create a dataframe
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
                    row_list=list(rows)
                    row_list=list( map(lambda x: x.get_row(), row_list))
                    df=pd.DataFrame(rows,columns=col)
                    df.to_csv("data.csv", index=False)
                    break

                encodedPayload=payload_manager.getEncodedPayload()
                keRequest= KeRequest(encodedPayload)
                data_list=keRequest.get_response()
                #Create Datarows from data
                new_rows=set ( map(lambda x: DataRow(x), data_list) )
                if len(rows.intersection(new_rows))> 0:
                    print("Duplicates found")
                    payload_manager.moveBlock()
                else:
                    payload_manager.moveCursortoNextPage()
                print("Rows length",len(rows))
                rows=rows.union(new_rows)
                   
               
        
       
class KeRequest:
    def __init__(self, encoded_payload:str):
        self.url="https://staging.ke.com.pk:8490/index.aspx"
        self.method="POST"
        self.timeout=5
        self.encoded_payload=encoded_payload


    def get_response(self):
        self.add_delay()
        response = requests.request(
                    self.method, self.url, headers=headers, data=self.encoded_payload, timeout=self.timeout)
        response=response.text
        pt= PostTransform(response)
        pt.process_data()
        data=pt.get_data()
        return data

    def add_delay(self):
        time.sleep(1)
       
            