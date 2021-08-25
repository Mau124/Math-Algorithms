"""Module for linear algebra

Brief description of the module and its purpose
A list of any classes, exception, functions, and any other objects exported by the module
"""
eps = 0.01

def matrix_form(A):
    print()
    for i in range(len(A)):
        for j in range(len(A[0])):
            print("{:.2f}".format(A[i][j]), end="\t")
        print()
    print()

def swap_rows(a, i, j):
    """This function swaps two columns of a matrix

    """
    for k in range(a.n):
        aux = a[i][k]
        a[i][k] = a[j][k] 
        a[j][k] = aux

def zeros(a, limit):
    """This functions counts the numbers of zeros in a list up to limit
   """
    cnt = 0
    for i in range(limit):
        if abs(a[i]) < eps:
            cnt+=1
    return cnt

def linear_solve(A, b):
    """This function solves a systems of algebraic linear equations
        
        A basic implementation of Gauss-Jordan 
    """
    # solutions give number of solutions. 0 if one exist, -1 if none and 1 if infinite
    solutions = 0
    for i in range(len(A)):
        A[i].append(b[i])

    pivot_i = 0
    pivot_j = 0
    exist_row = False

    while pivot_i < len(A):
        # Find a valid pivot_i and pivot_j
        exist_row = False
        while pivot_j < len(A[0])-1:
            if A[pivot_i][pivot_j] == 0:
                for i in range(pivot_i+1, len(A)):
                    if A[i][pivot_j] != 0:
                        swap_rows(A, pivot_i, i)
                        exist_row = True
                if not exist_row:
                    pivot_j+=1
            else:
                exist_row = True
                break

        if not exist_row:
            break

        # Make all elements in that column 0s
        for row in range(len(A)):
            if row != pivot_i:
                tmp = A[row][pivot_j]/A[pivot_i][pivot_j]
                for col in range(len(A[0])):
                    A[row][col] = A[row][col] - tmp*A[pivot_i][col]

        pivot_i+=1
        pivot_j+=1

    for i in range(len(A)):
        tmp=A[i][i]
        if tmp!=0:
            for j in range(len(A[0])):
                A[i][j]/=tmp

    var = 0
    ans = []
    matrix_form(A)
    for i in range(len(A)):
        n_zeros = zeros(A[i], len(A[0])-1)
        if n_zeros == len(A[0])-2:
            var+=1
            ans.append(round(A[i][-1], 2))
        elif n_zeros == len(A[0])-1:
            if A[i][-1] != 0:
                # El sistema no tiene solucion
                solutions = -1
                break

    if solutions != -1:
        if var == len(A[0])-1:
            solutions = 0
        else:
            solutions = 1

    return [solutions, ans]
