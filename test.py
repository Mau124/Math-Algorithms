from linalg import *

def printVec(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print("")

# Example 1
A = [[5], [4]]
b = [10, 8]
ans = linear_solve(A, b)
print("Case 1")
print(ans)

# Example 2
A = [[1, -1, 3],
     [1, 1, 1],
     [2, 2, -1]]
b = [13, 11, 7]
ans = linear_solve(A, b)
print("Case 2")
print(ans)

# Example 3
A = [[2, 3, 4],
     [2, 6, 8],
     [4, 9, -4]]
b = [3, 5, 4]
ans = linear_solve(A, b)
print("Case 3")
print(ans)

# Example 4
A = [[2, -1, 3],
     [2, 2, 3],
     [-2, 3, 0]]
b = [5, 7, -3]
ans = linear_solve(A, b)
print("Case 4")
print(ans)

# Example 5
A = [[2, 6, 1],
     [1, 2, -1],
     [5, 7, -4]]
b = [7, -1, 9]
ans = linear_solve(A, b)
print("Case 5")
print(ans)

# Example 6
A = [[3, -2, 5],
     [2, 4, -1],
     [-7, -3, 4]]
b = [38, -7, 5]
ans = linear_solve(A, b)
print("Case 6")
print(ans)

# Cases with infinite solutions
A = [[1, 1, 1],
     [2, 4, 1],
     [6, 10, 4]]
b = [3, 8, 22]
ans = linear_solve(A, b)
print("Case 7")
print(ans)

A = [[1, 1, 2],
     [2, -1, 1],
     [4, 1, 5]]
b = [1, 2, 4]
ans = linear_solve(A, b)
print("Case 8")
print(ans)

# Cases with no solution
A = [[1, 1, -1],
     [2, 3, -1],
     [3, 4, -2]]
b = [2, 0, 1]
ans = linear_solve(A, b)
print("Case 9")
print(ans)

# Case 10 does not work
A = [[2, 5, -5],
     [4, 10, -8]]
b = [36, -16]
ans = linear_solve(A, b)
print("Case 10")
print(ans)

A = [[1, 1, 1],
     [3, -2, -2],
     [4, -1, -1]]
b = [4, -3, 0]
ans = linear_solve(A, b)
print("Case 11")
print(ans)
