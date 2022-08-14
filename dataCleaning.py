from typing import List
import re
from bs4 import BeautifulSoup


def clean_from_text(data: str) -> List:

    data = data.text

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
    return e
