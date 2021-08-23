"""Matrix type
"""
from real import Real

class Matrix:
    """Comments
    """
    def __init__(self, mat):
        self.n = len(mat)
        self.m = len(mat[0])
        self.matrix = []

        for i in range(self.n):
            tmp = []
            for j in range(self.m):
                tmp.append(Real(mat[i][j]))
            self.matrix.append(tmp)

    def __repr__(self):
        print()
        for i in range(self.n):
            print("|", end="\t")
            for j in range(self.m):
                print(f'{self.matrix[i][j]}', end="\t")
            print("|")
        print()
