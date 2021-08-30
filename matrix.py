"""
    TODO:
        Comments
"""
class Matrix:

    def __init__(self, Aux):
        """Constructor a Matrix class. It takes a list o lists as parameter"""
        self.n = len(Aux)

        if isinstance(Aux[0], list):
            self.m = len(Aux[0])
        else:
            self.m = 1 

        self.A = []
        for i in range(self.n):
            if isinstance(Aux[i], list):
                self.A.append(Aux[i])
            else:
                self.A.append([Aux[i]])

    @classmethod
    def from_dims(cls, rows, cols) -> 'Matrix':
        A = [[0] * cols for i in range(rows)]
        return cls(A)
        

    def __add__(self, B):
        """Matrix addition. Returns the result of A + B"""
        if self.n != B.n or self.m != B.m:
            raise ValueError('Matrices must have same dimensions')

        C = []
        for i in range(self.n):
            tmp = []
            for j in range(self.m):
                tmp.append(self[i, j] + B[i, j])
            C.append(tmp)

        return Matrix(C)

    def __sub__(self, B):
        """Matrix substraction. Returns the result of A - B"""
        if self.n != B.n or self.m != B.m:
            raise ValueError('Matrices must have same dimensions')

        C = []
        for i in range(self.n):
            tmp = []
            for j in range(self.m):
                tmp.append(self[i, j] - B[i, j])
            C.append(tmp)

        return Matrix(C)

    def __mul__(self, c):
        """Multiplication by scalar. Returns the result of c * A"""
        if not (isinstance(c, int) or isinstance(c, float)):
            raise ValueError('Multiplication is by an scalar')

        C = []

        for i in range(self.n):
            tmp = []
            for j in range(self.m):
                tmp.append(self[i, j] * c)
            C.append(tmp)
            
        return Matrix(C)

    def __rmul__(self, c):
        """Multiplication by scalar. Returns the result of c * A"""
        return self.__mul__(c)

    def __matmul__(self, B):
        """Matrix multiplication. Returns the result of A * B"""
        if self.m != B.n:
            raise ValueError('Columns of first Matrix needs to match with rows of second Matrix')

        C = Matrix.from_dims(self.n, B.m)
        for i in range(self.n):
            for j in range(B.m):
                aux = 0
                for k in range(self.m):
                    aux += (self[i,k]*B[k,j])
                C[i, j] = aux

        return C

    def trans(self):
        C = Matrix.from_dims(self.m, self.n)

        for i in range(self.n):
            for j in range(self.m):
                C[j, i] = self[i, j]
        return C


    def __getitem__(self, index):
        """Return the item that is in the position index"""
        if isinstance(index, tuple):
            i = index[0]
            j = index[1]
            return self.A[i][j]

        if isinstance(index, int):
            return self.A[index]

    def __setitem__(self, index, value):
        """Change the value of the item in position index with value"""
        if isinstance(index, tuple):
            i = index[0]
            j = index[1]
            self.A[i][j] = value 
    
    def __repr__(self):  
        """Return a string with the representation of a matrix"""
        mt_str = ''
        for i in range(self.n):
            mt_str += '|\t'
            for j in range(self.m):
                mt_str += str(self.A[i][j]) + '\t'
            mt_str += '|\n'

        return mt_str
    
def dot_product(A, B):
    """Return the dot product of Matrix A and B"""
    if A.n != B.n or A.m != 1 or B.m != 1:
        raise ValueError('Cannot perfom dot product on those vectors')

    return (A.trans() @ B)[0, 0]

def cross_product(A, B):
    """Return the cross producto of Matrix A and B"""
    if A.n != B.n or A.m != 1 or B.m != 1:
        raise ValueError('Cannot perfomr cross product on those vector')


