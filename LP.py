""" Module for Linear programming

    This file contains algorithms for linear programming. It has a basic set of 
    algorithms that are taught in a linear programming basic course. 

    The code is a mess and the next update is to merge code with linalg, so it is
    not so messy. 
"""
import copy
from re import U
import numpy as np

INF = 200

def print_matrix(M):
    rows, cols = M.shape

    print()
    for row in range(rows):
        for col in range(cols):
            print(f'{M[row,col]:.2f}\t', end="")
        print()
    print()


def gauss_jordan_LP(A, maximize):
    """ Gauss jordan with LP """
    M = copy.deepcopy(A) 
    aux_array = np.zeros(len(M[0])-2)

    print("--------- Matrix original ----------")
    print_matrix(M)

    # Eliminar M's que estan en variables artificiales
    indexes_M = M[0, :-1] == INF

    print("--------- Eliminar M's -------------")
    print()
    it = 0
    for i in range(len(indexes_M)):
        if indexes_M[i] == True:
            # Search for a value to be a pivot
            pivot = 1
            while M[pivot][i] == 0:
                pivot += 1

            print(f"Eliminar {it} M")
            tmp = M[0][i]/M[pivot][i]

            for col in range(M.shape[1]):
                M[0][col] = M[0][col] - tmp*M[pivot][col]

            print_matrix(M)
            it += 1
                   
    print("--------- Resolver -------------")
    print()
    it = 0

    if maximize:
        is_not_optimal = np.any(M[0, 1:-1] < aux_array)
    else:
        is_not_optimal = np.any(M[0, 1:-1] > aux_array)

    while is_not_optimal: 
        # Gauss jordan algo

        # Get most negative in first row to obtain the col
        if maximize:
            pivot_col = np.argmin(M[0, :-1])
        else:
            pivot_col = np.argmax(M[0,:-1])

        ratio = 10000
        pivot_row = -1

        for i in range(1, M.shape[0]):
            if M[i, pivot_col] != 0:
                tmp = M[i,-1]/M[i,pivot_col]
                if tmp >= 0 and tmp < ratio:
                    ratio = tmp
                    pivot_row = i

        # Make M[pivot_row][pivot_col] = 1
        print("Iteracion: ", it)

        tmp = M[pivot_row][pivot_col]
        if tmp != 0:
            M[pivot_row] = M[pivot_row]/tmp

            # DO gauss jordan with those iterators
            for row in range(M.shape[0]):
                if row != pivot_row:
                    if M[pivot_row][pivot_col] != 0:
                        tmp = M[row][pivot_col]/M[pivot_row][pivot_col]
                        for col in range(M.shape[1]):
                            M[row][col] = M[row][col] - tmp*M[pivot_row][col]

                        print(f"Row {row} = row {row} - {tmp:.2f} * row {pivot_row}")

        print_matrix(M)                     

        if maximize:
            is_not_optimal = np.any(M[0, 1:-1] < aux_array)
        else:
            is_not_optimal = np.any(M[0, 1:-1] > aux_array)

        it += 1

    return M