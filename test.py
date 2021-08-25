from linalg import *
from real import Real
from matrix import Matrix

def printVec(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print("")

A = Matrix([[1, 0, -2],
            [-2, 1, 3],
            [0, -1, 1]])

b = Matrix([1, 1, 1])

# print(a)

ans = linear_solve(A, b)
print(ans)
