
import csv
import re
import time
from typing import List
from DataRow import DataRow
from example_payload import PayloadProcessor
import requests
from bs4 import BeautifulSoup

       
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Origin': 'https://staging.ke.com.pk:8490',
    'Pragma': 'no-cache',
    'Referer': 'https://staging.ke.com.pk:8490/index.aspx',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-gpc': '1'
}


def make_Request_to_api(encoded_payload:str)->List:
     response = requests.request(
                                    "POST",
                                    "https://staging.ke.com.pk:8490/index.aspx",
                                    headers=headers,
                                    data=encoded_payload,
                                    timeout=5,
                                )
     return response.text
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
    post_payload=get_encoded_post_payload(page, block)
    data=make_Request_to_api(post_payload)
    list_of_rows=extract_table_from_text(data)
    return list_of_rows

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


def extract_table_from_text(text:str)->List:
        data=text
        if data[0:7] == '0|/*DX*':
            print("Response type: json\n")
        else:
            raise Exception("Response type: html\n")


        testdata = data[20:-10]
        regular_expression = r"<tr id=\"uploadGrd_DXDataRow\d+\" class=\"dxgvDataRow_Aqua\">"
        l = re.split(regular_expression, testdata)

        e = []
        for i in range(1, len(l)):
            table_data = BeautifulSoup(l[i], features="lxml").find_all("td")
            c = []
            for table_row in table_data:
                c.append(table_row.text)
            e.append(c)
        lists=e

        rows=[]
        for row in  lists:
            if len(row)==22:
                #Break it up into two lists of 11 elements
                row1=row[:11]
                row2=row[11:]
                rows.append(row1)
                rows.append(row2)
            else:
                rows.append(row)

        data=rows

        data = [x[1:] for x in data]

        return data




if __name__ == "__main__":
    data=get_page(144)
    print(data)


