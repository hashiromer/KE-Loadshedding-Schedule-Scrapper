import pandas as pd
from DataRow import DataRow
from KERequest import KeRequest
from formOptions import PayloadManager


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
                   
               
        
       
