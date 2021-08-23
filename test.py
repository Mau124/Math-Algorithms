from linalg import *
from real import Real
from matrix import Matrix

def printVec(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print("")

a = [[2, -1, 3],
     [2, 2, 3],
     [-2, 3, 0]]

b = [[5], [7], [-3]]

# print(a)

ans = linear_solve(a, b)
