class DataRow:

    def __init__(self, row) -> None:
        self.row=tuple(row)

    def __hash__(self):
        st= ''.join(self.row)
        return hash(st)

    def __eq__(self, other):
        return self.row == other.row

    def get_row(self):
        return self.row



if __name__ == "__main__":

    #Create a list of DataRows
     row1=["ab","cd","ef"]
     row2=["jb","ld","ef"]
     row3=["ab","cd","ef"]

     Datarows=set(map(lambda x: DataRow(x), [row1,row2,row3]))

     print(len(Datarows))
    