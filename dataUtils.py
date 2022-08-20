
import csv
import re
import time
from typing import List
from DataRow import DataRow
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


session_object=requests.Session()


def get_post_payload(options:dict) -> str:
    form_body_data={
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__VIEWSTATE": "75bMG2iqZw68TRb9R%2BHHUJSZH7GrEdwuDANza%2F1gsiINbPQ8317qddj1VnAZ%2BwMm8nNpRmLuW1nj6g2BgUkkhuUv1dozcz0TvRK3F%2BfQsbHFAnqAxAa7cgeAvhIURkbp1Do7nwPD8%2F1gMMnqTr5RzcfldcyFWIvVzn6p9F3DlMLKsg4%2F6Q2G8qauX3EOk7B2yKumzPW4DpFhXDBEXZsCAQ7Q%2FieWIxqrIVhynrbF6%2Fs%3D",
    "__VIEWSTATEGENERATOR": "90059987",
    "uploadGrd$DXFREditorcol1": "",
    "uploadGrd$DXFREditorcol2": "",
    "uploadGrd$DXFREditorcol3": "",
    "uploadGrd$DXFREditorcol4": "",
    "uploadGrd$DXFREditorcol5": "",
    "uploadGrd$DXFREditorcol6": "",
    "uploadGrd$DXFREditorcol7": "",
    "uploadGrd$DXFREditorcol8": "",
    "uploadGrd$DXFREditorcol9": "",
    "uploadGrd$DXFREditorcol10": "",
    "uploadGrd$DXSelInput": "",
    "uploadGrd$DXKVInput:": "[]",
    "uploadGrd$CallbackState":"BwQHAgIERGF0YQbyBAAAAAClBQAApQUAAAoAAAAKAAAAAAoAAAAFR3JpZHMFR3JpZHMHAAALU3dpdGNoX05hbWULU3dpdGNoX05hbWUHAAAGR3JvdXBzBkdyb3VwcwcAAAhDYXRlZ29yeQhDYXRlZ29yeQcAAAtGaXJzdF9DeWNsZQtGaXJzdF9DeWNsZQcAAAxTZWNvbmRfQ3ljbGUMU2Vjb25kX0N5Y2xlBwAAC1RoaXJkX0N5Y2xlC1RoaXJkX0N5Y2xlBwAAC0ZvcnRoX0N5Y2xlC0ZvcnRoX0N5Y2xlBwAAC0ZpZnRoX0N5Y2xlC0ZpZnRoX0N5Y2xlBwAAC1NpeHRoX0N5Y2xlC1NpeHRoX0N5Y2xlBwAAAQAAAAJJRAcABwAHAAcABv%2F%2FBwIJQUdIQSBLSEFOBwINU0hBTUlNIEFITUVEIAcCATQHAglOb3JtYWwtTEwHAgkxMzM1fjE1MDUHAgkwMzA1fjA1MDUHAgEtBwIBLQcCAS0HAgEtBwAHAAb%2F%2FwcCCUFHSEEgS0hBTgcCC1NVTk5ZIFZPSFJBBwIBMQcCCU5vcm1hbC1MTAcCCTA5MDV%2BMTAzNQcCCTAxMDV%2BMDMwNQcCAS0HAgEtBwIBLQcCAS0HAAcABv%2F%2FBwIHQUlSUE9SVAcCGFNVUEVSSU9SIFNJQ0VOQ0UgQ09MTEVHRQcCATIHAgZDT04tTEwHAgkxMDM1fjEyMDUHAgkxNzA1fjE4MzUHAgkwMTA1fjAyMDUHAgkwMzA1fjA0MDUHAgEtBwIBLQcABwAG%2F%2F8HAgdBSVJQT1JUBwILVEFOR0EgU1RBTkQHAgExBwIGQ09OLUxMBwIJMDkwNX4xMDM1BwIJMTYwNX4xNzM1BwIJMDEwNX4wMjA1BwIJMDMwNX4wNDA1BwIBLQcCAS0HAAcABv%2F%2FBwIHQUlSUE9SVAcCFVNJRERJUUlBIE1BU0pJRCBSTVUgKwcCATMHAgZDT04tTEwHAgkxMjA1fjEzMzUHAgkxNzM1fjE5MDUHAgkwMTA1fjAyMDUHAgkwMzA1fjA0MDUHAgEtBwIBLQcABwAG%2F%2F8HAgdBSVJQT1JUBwIPU0hBTUEgQ0VOVFJFICArBwIBMgcCCU5vcm1hbC1MTAcCCTEwMzV%2BMTIwNQcCCTAxMDV%2BMDMwNQcCAS0HAgEtBwIBLQcCAS0HAAcABv%2F%2FBwIHQUlSUE9SVAcCF1NIT1VLQVQgVU1BUiBIT1NQSVRBTCArBwIBOQcCBkNPTi1MTAcCCTEzMDV%2BMTQzNQcCCTE3MzV%2BMTkwNQcCCTAwMDV%2BMDEwNQcCCTA1MDV%2BMDYwNQcCAS0HAgEtBwAHAAb%2F%2FwcCB0FJUlBPUlQHAg1TQU5HQU0gQ0lORU1BBwIBNgcCBkNPTi1MTAcCCTE1MzV%2BMTcwNQcCCTIwMzV%2BMjIwNQcCCTAwMDV%2BMDEwNQcCCTAyMDV%2BMDMwNQcCAS0HAgEtBwAHAAb%2F%2FwcCB0FJUlBPUlQHAgVRRUMgKwcCATYHAglOb3JtYWwtTEwHAgkxNjM1fjE4MDUHAgkwMzA1fjA1MDUHAgEtBwIBLQcCAS0HAgEtBwAHAAb%2F%2FwcCB0FJUlBPUlQHAgtSRVRBIFBMT1QgKwcCAjNjBwICSEwHAgkwODA1fjEwMzUHAgkxMzA1fjE2MDUHAgkxODM1fjIxMDUHAgkyMzA1fjAxMDUHAgEtBwIBLQIFU3RhdGUHXQcLBwACAQcBAgEHAgIBBwMCAQcEAgEHBQIBBwYCAQcHAgEHCAIBBwkCAQcKAgEHAAcABwAHAAIABQAAAIAJAgAHAAkCAAIAAwcEAgAHAAIBBqUFBwACAQcABwAHAAINU2hvd0ZpbHRlclJvdwoCAQIJUGFnZUluZGV4AwcB",
    "DXScript":"1_171,1_94,1_164,1_104,1_138,1_114,1_121,1_152",
    "DXCss":" 0_108,0_260,1_12,0_110,0_264,0_100,1_5,0_102",
    "__CALLBACKID":"uploadGrd",
    "__CALLBACKPARAM":"c0:KV|2;[];GB|20;12|PAGERONCLICK3|PN5",
    "__EVENTVALIDATION":"ryBIH+GqwwiR5H8miIbcIgtdiuImx9XcWZfIJv9GMVoWfbDYJQqUYG3PsHfekIA3Gu0cfKl0CeG4EFsT5sM6CzYEUmaIa71F+FZ57nFxtDygvTTzYUnneLSjy6V1mESF"

    


}

    #Add options to form_body_data

    for key, value in options.items():
        form_body_data[key]=value




    t = []
    for key, value in form_body_data.items():
        if key == '__VIEWSTATE' or key == 'uploadGrd$CallbackState':
            k = quote(key)
            v = value
        else:
            k = quote(key)
            v = quote(value)

        st = k+'='+v
        t.append(st)

    split = '&'.join(t)
    return split

def make_Request_to_api(encoded_payload:str)->List:
    

    headers=  {
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
    },

    #Send request with sessions object
    url="https://staging.ke.com.pk:8490/index.aspx"
    response=session_object.post(url, data=encoded_payload, headers=headers[0],timeout=5)
    return response.text
def get_encoded_post_payload(page:int, PAGERONCLICK:int)->str:
    
    options={}
    rangeStart=20+PAGERONCLICK-3
    options= {
    '__CALLBACKPARAM':  f"c0:KV|2;[];GB|{rangeStart};12|PAGERONCLICK{PAGERONCLICK}|PN{page};"
        }
    payload=get_post_payload(options)
    return payload

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
    total_rows=[]
    for page in range(total_pages):
        print(f"Fetching Page: {page}")
        data_list=get_page(page)
        total_rows.extend(data_list)
   
    schedule=list(set ( map(lambda x: DataRow(x), total_rows) ))
    schedule=list(map(lambda x: x.get_row(), schedule))
    return schedule

def save_to_disk(data:list[DataRow]):
   #Convert datarows to rows

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
        if data[0:7] != '0|/*DX*':
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
    data=get_load_shedding_schedule()
    print (len(data))
    save_to_disk(data)


