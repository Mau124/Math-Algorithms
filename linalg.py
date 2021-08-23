"""Module for linear algebra

Brief description of the module and its purpose
A list of any classes, exception, functions, and any other objects exported by the module
"""
def matrix_form(a):
    print("A: ")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='\t')
        print("")
    print("")

def swap_rows(a, i, j):
    """This function swaps two columns of a matrix

    """
    for k in range(len(a[i])):
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
    for row in range(len(a)):
        a[row].append(b[row])

    pivot_i = 0
    pivot_j = 0
    exist_row = False

    while pivot_i < len(a):
        # Find a valid pivot_i and pivot_j
        exist_row = False
        while pivot_j < len(a[pivot_i])-1:
            if a[pivot_i][pivot_j] == 0:
                for i in range(pivot_i+1, len(a)):
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
        for row in range(len(a)):
            if row != pivot_i:
                matrix_form(a)
                print(f'{a[row][pivot_j]} / {a[pivot_i][pivot_j]}')
                tmp = a[row][pivot_j]/a[pivot_i][pivot_j]
                for col in range(len(a[row])):
                    print(f'{a[row][col]} - {tmp}*{a[pivot_i][col]}')
                    a[row][col] = a[row][col] - tmp*a[pivot_i][col]


        pivot_i+=1
        pivot_j+=1

    for i in range(len(a)):
        tmp=a[i][i]
        if tmp!=0:
            for j in range(len(a[i])):
                a[i][j]/=tmp

    var = 0
    for i in range(len(a)):
        n_zeros = zeros(a[i], len(a[i])-1)
        if n_zeros == len(a[i])-2:
            var+=1
        elif n_zeros == len(a[i])-1:
            if a[i][-1] != 0:
                # El sistema no tiene solucion
                solutions = -1
                break

    print("Solutions founded: ", var)
    if solutions == -1:
        print("There is no solution for the system")
        matrix_form(a)
    else:
        if var == len(a[0])-1:
            print("There is one unique solution")
            matrix_form(a)
        else:
            print("There are infinite solutions")
            matrix_form(a)
