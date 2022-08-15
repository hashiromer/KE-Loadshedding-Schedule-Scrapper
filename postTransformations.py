
import csv
from typing import List


class PostTransform:
    def __init__(self, li:List[List]):

        rows=[]
        for row in  li:
            if len(row)==22:
                #Break it up into two lists of 11 elements
                row1=row[:11]
                row2=row[11:]
                rows.append(row1)
                rows.append(row2)
            else:
                rows.append(row)

        self.data=rows

            


        #Remove first column from list of lists
        self.data = [x[1:] for x in self.data]




    

    def to_csv(self,filename:str):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.data)
      