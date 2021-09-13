import matrix as mat
import linalg as lin

def printVec(a):
    for i in range(len(a)):
        print(a[i], end=" ")
    print("")

A = mat.Matrix([[1, -1, 3], [1, 1, 1], [2, 2, -1]])
b = mat.Matrix([13, 11, 7])
C = lin.linear_solve(A, b)
print("Matriz con respuesta")
print(C[1])

