""" Module for linear algebra

    This file contains algorithms for linear algebra. It has a basic set of 
    algorithms that are taught in a linear algebra basic course. It has
    only educational purposes. 
"""
import copy
import matrix as mat

def matrix_form(A):
    print()
    for i in range(len(A)):
        for j in range(len(A[0])):
            print("{:.2f}".format(A[i][j]), end="\t")
        print()
    print()

def swap_rows(A, index1, index2):
    """ This function swaps two rows of a matrix"""
    aux = A[index1]
    A[index1] = A[index2]
    A[index2] = aux

def gauss_jordan(A):
    """ This function reduces a matrix A into a reduced echelon form using 
        gauss jordan as the algorithm
        It returns a matrix M that is a reduced matrix of A """
    M = copy.deepcopy(A)

    for pivot in range(len(M)):
        # Find a valid pivot_i and pivot_j
        if M[pivot][pivot] == 0:
            for i in range(pivot+1, len(M)):
                if M[i][pivot] != 0:
                    swap_rows(M, pivot, i)
                    break

        if M[pivot][pivot] != 0:
            # Make all elements in that column 0s
            for row in range(len(M)):
                if row != pivot:
                    tmp = M[row][pivot]/M[pivot][pivot]
                    for col in range(len(M[0])):
                        M[row][col] = M[row][col] - tmp*M[pivot][col]

    return M

def linear_solve(A, b):
    """ Solve a system of linear equations
        It takes a coefficient matrix A and a vector of dependent variables b
        It returns a tuple with (-1, 0, 1) value in the first value of the tuple
        -1: If the system has no solution
        0: If the system has a unique solution
        1: If the system has infinite solutions
        The second value of the tuple is a list with the values that satisfy the
        equation. It returns an empty list if the system has no solution or has
        infinite """
    eps = 0.01
    solutions = 0
    ans = []
    M = copy.deepcopy(A)

    for i in range(len(M)):
        M[i].append(b[i])

    M = gauss_jordan(M)
    for row in range(len(M)):
        tmp = M[row][row]
        if abs(tmp) > eps:
            M[row][:] = [n/tmp for n in M[row]]

        zeros = sum(abs(i) < eps for i in M[row][:-1])
        if zeros == len(M[row][:-1])-1:
            solutions += 1
            ans.append(round(M[row][-1], 4))
        elif zeros  == len(M[row][:-1]) and M[row][-1] != 0:
            return (-1, [])

    if solutions == len(M[0])-1:
        return (0, ans)
    else:
        return (1, [])

def det(A):
    """Returns the determinant of a matrix A"""
    mat = gauss_jordan(A)
    det = 1
    for i in range(len(mat)):
        det *= mat[i][i]
    return  round(det, 4)

def inv(A):
    pass

def tra(A):
    pass

def isorthogonal_set(v):
    """ Returns True if the list of vectors passed as parameters are orthogonal,
        False otherwise"""
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            if mat.dot_product(v[i], v[j]) != 0:
                return False
    return True

def basis(A):
    pass

def islinearly_dependent(V):
    pass

def gram_schmidt(V):
    pass
