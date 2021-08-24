"""Matrix type
"""
from real import Real

class Matrix:
    """Comments
    """
    def __init__(self, A):
        self.n = len(A)

        if isinstance(A[0], list):
            self.m = len(A[0])
        else:
            self.m = 1

        self.matrix = []

        for i in range(self.n):
            tmp = []
            if isinstance(A[i], list):
                for j in range(self.m):
                    tmp.append(Real(A[i][j]))
            else:
                tmp.append(Real(A[i]))
            self.matrix.append(tmp)

    def __getitem__(self, index):
        return self.matrix[index]

    def add_col(self, col):
        if len(col) == self.n:
            for i in range(self.n):
                if isinstance(col[i], list):
                    return -1
                self[i].append(Real(col[i]))   
            self.m += 1
        else:
            return -1

    def add_row(self, row):
        if len(row) == self.m:
            tmp = []
            for i in range(self.m):
                if isinstance(row[i], list):
                    return -1
                tmp.append(Real(row[i]))
            self.matrix.append(tmp)
            self.n += 1
        else:
            return -1

    def __repr__(self):
        print()
        for i in range(self.n):
            print("|", end="\t")
            for j in range(self.m):
                print(f'{self.matrix[i][j]}', end="\t")
            print("|")
        print()
        return ""
