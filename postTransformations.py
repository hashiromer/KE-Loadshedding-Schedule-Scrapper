
import csv
from typing import List
import re
from bs4 import BeautifulSoup

class PostTransform:
    def __init__(self,text:str):
        self.lists=None
        self.data=None
        self.text=text


    def text_to_list(self):
        data=self.text
        if data[0:7] == '0|/*DX*':
            print("--------- type is json------------\n")
        else:
            print("--------- type is html------------\n")

        testdata = data[20:-10]
        regular_expression = r"<tr id=\"uploadGrd_DXDataRow\d+\" class=\"dxgvDataRow_Aqua\">"
        l = re.split(regular_expression, testdata)

        e = []
        for i in range(1, len(l)):
            table_data = BeautifulSoup(l[i], features="html").find_all("td")
            c = []
            for table_row in table_data:
                c.append(table_row.text)
            e.append(c)
        self.lists=e




    def list_to_rows(self):
        rows=[]
        for row in  self.lists:
            if len(row)==22:
                #Break it up into two lists of 11 elements
                row1=row[:11]
                row2=row[11:]
                rows.append(row1)
                rows.append(row2)
            else:
                rows.append(row)

        self.data=rows

        self.data = [x[1:] for x in self.data]


    def process_data(self):
        self.text_to_list()
        self.list_to_rows()
    

    def to_csv(self,filename:str):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.data)
      
    def get_data(self):
        return self.data