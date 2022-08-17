class DataRow:

    def __init__(self, row) -> None:
        self.row=tuple(row)

    def __hash__(self):
        return ''.join(self.row).__hash__()