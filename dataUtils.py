
import csv
import time
from typing import List
from DataRow import DataRow
from example_payload import PayloadProcessor,headers
from postTransformations import PostTransform
import requests
       


def make_Request_to_api(encoded_payload:str)->List:
     response = requests.request(
                                    "POST",
                                    "https://staging.ke.com.pk:8490/index.aspx",
                                    headers=headers,
                                    data=encoded_payload,
                                    timeout=5,
                                )
     pt= PostTransform(response.text)
     pt.process_data()
     data=pt.get_data()
     return data





def get_encoded_post_payload(page:int, PAGERONCLICK:int)->str:
    payload_processor=PayloadProcessor()
    options={}
    rangeStart=20+PAGERONCLICK-3
    options= {
    '__CALLBACKPARAM':  f"c0:KV|2;[];GB|{rangeStart};12|PAGERONCLICK{PAGERONCLICK}|PN{page};"
        }
    payload_processor.add_options_to_payload(options)
    return payload_processor.getPayload()

def get_block(page:int)->int:

    if page >=0 and page <10:
        return 3
    elif page >=10 and page <100:
        return 4
    elif page >=100 and page <145:
        return 5
    else:
        raise Exception("Page number out of range")

def get_page(page:int):
    block=get_block(page)
    payload=get_encoded_post_payload(page, block)
    data=make_Request_to_api(payload)
    return data

    

    


def get_load_shedding_schedule():
    total_pages=145
    tot_rows=[]
    for page in range(total_pages):
        time.sleep(2)
        print(f"Page: {page}")
        data_list=get_page(page)
        tot_rows.extend(data_list)
   
    data=list(set ( map(lambda x: DataRow(x), tot_rows) ))
    return data

   


def save_to_disk(data:list[DataRow]):
   #Convert datarows to rows
    data=list(map(lambda x: x.get_row(), data))

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
    print("total rows: ", len(data))
    with open('data.csv','w') as out:
            csv_out=csv.writer(out)
            csv_out.writerow(col)
            for row in data:
                csv_out.writerow(row)


if __name__ == "__main__":
    data=get_page(144)
    print(data)


