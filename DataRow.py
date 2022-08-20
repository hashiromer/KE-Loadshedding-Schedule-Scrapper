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
    

