import pandas as pd
import requests
from DataRow import DataRow
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
                    df=pd.DataFrame(rows,columns=col)
                    df.to_csv("data.csv", index=False)
                    break


                encodedPayload=payload_manager.getEncodedPayload()
                url = "https://staging.ke.com.pk:8490/index.aspx"
                response = requests.request(
                    "POST", url, headers=headers, data=encodedPayload, timeout=5)
                response=response.text



                pt= PostTransform(response)
                pt.process_data()

                data=pt.get_data()

                #Create Datarows from data
                new_rows=set ( map(lambda x: DataRow(x), data) )
                # new_rows=set(map(set,data))
                # data=pd.DataFrame(data, columns=col)
                if len(rows.intersection(new_rows))> 0:
                    print("Duplicates found")
                    payload_manager.moveBlock()
                else:
                    payload_manager.moveCursortoNextPage()
                print("Rows length",len(rows))
                rows=rows.union(new_rows)
                print(list(rows)[-1])    
                   
               
        
       
       
            