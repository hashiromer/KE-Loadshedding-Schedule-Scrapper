from DataRow import DataRow
from KERequest import KeRequest
from formOptions import PayloadManager
import csv


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
                print(f"\n-----------Iteration Count: {count}---------------")
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

                    with open('data.csv','w') as out:
                        csv_out=csv.writer(out)
                        csv_out.writerow(col)
                        for row in row_list:
                            csv_out.writerow(row)

                    break

                encodedPayload=payload_manager.getEncodedPayload()
                keRequest= KeRequest(encodedPayload)
                data_list=keRequest.get_response()
                #Create Datarows from data
                new_rows=set ( map(lambda x: DataRow(x), data_list) )
                if len(rows.intersection(new_rows))> 0:
                    print(f"~~~Duplicates found at page: {payload_manager.getPage()}, PageOnClick: {payload_manager.getBlock()}")
                    print("Total new rows found: ", len(new_rows- rows))
                    payload_manager.moveBlock()
                else:
                    print(f"{len(new_rows)} new values found at page: {payload_manager.getPage()}, PageOnClick: {payload_manager.getBlock()}")
                    payload_manager.moveCursortoNextPage()

                
                rows=rows.union(new_rows)
                print(f"Total Distinct Rows found so far: {len(rows)}")
                   
# class DatRowSet:
#     def __init__(self, list_of_rows=None):
#         if list_of_rows is None:
#             self.rows=set()
#         else:
#             self.rows=set(list_of_rows)

#     def add(self, row):
#         self.rows.add(row)

#     def get_rows(self):
#         return self.rows

#     def total_rows(self):
#         return len(self.rows)               
        
       
