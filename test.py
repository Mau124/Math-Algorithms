from linalg import *

def printVec(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print("")

def change(a):
    for i in range(len(a)):
        a[i]+=1

a = [[3, 5, 1],
     [3, 1, -7],
     [1, 3, 3]]

b = [0, 0, 0]

ans = solve(a,b)

