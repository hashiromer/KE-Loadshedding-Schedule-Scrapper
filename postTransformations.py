
import csv
from typing import List


class PostTransform:
    def __init__(self, li:List[List]):
        self.data = li

        #Remove first column from list of lists
        self.data = [x[1:] for x in self.data]

        #Print length of list of lists

        for i in self.data:
            print(len(i))


    

    def to_csv(self,filename:str):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.data)
      