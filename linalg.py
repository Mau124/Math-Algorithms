"""Module for linear algebra

Brief description of the module and its purpose
A list of any classes, exception, functions, and any other objects exported by the module
"""
from matrix import Matrix

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
        if a[i] == 0:
            cnt+=1
    return cnt

def linear_solve(a, b):
    """This function solves a systems of algebraic linear equations
        
        A basic implementation of Gauss-Jordan 
    """
    # solutions give number of solutions. 0 if one exist, -1 if none and 1 if infinite
    solutions = 0
    a.add_col(b)

    pivot_i = 0
    pivot_j = 0
    exist_row = False

    while pivot_i < a.n:
        # Find a valid pivot_i and pivot_j
        exist_row = False
        while pivot_j < a.m-1:
            if a[pivot_i][pivot_j] == 0:
                for i in range(pivot_i+1, a.n):
                    if a[i][pivot_j] != 0:
                        swap_rows(a, pivot_i, i)
                        exist_row = True
                if not exist_row:
                    pivot_j+=1
            else:
                exist_row = True
                break

        if not exist_row:
            break

        # Make all elements in that column 0s
        for row in range(a.n):
            if row != pivot_i:
                tmp = a[row][pivot_j]/a[pivot_i][pivot_j]
                for col in range(a.m):
                    a[row][col] = a[row][col] - tmp*a[pivot_i][col]

        print(a)

        pivot_i+=1
        pivot_j+=1

    for i in range(a.n):
        tmp=a[i][i]
        if tmp!=0:
            for j in range(a.m):
                a[i][j]/=tmp
    var = 0
    for i in range(a.n):
        n_zeros = zeros(a[i], a.m-1)
        if n_zeros == a.m-2:
            var+=1
        elif n_zeros == a.m-1:
            if a[i][-1] != 0:
                # El sistema no tiene solucion
                solutions = -1
                break

    ans = []
    if solutions != -1:
        if var == a.m-1:
            for i in range(a.n):
                ans.append(a[i][-1])
            solutions = 0
        else:
            solutions = 1

    return [solutions, ans]
