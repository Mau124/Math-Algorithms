"""This file is for matrices operations

"""
def dot_product(A, B):
    ans = 0
    for i in range(len(A)):
        ans += (A[i]*B[i])
    return ans

def add(A, B):
    ans = []
    for i in range(len(A)):
        tmp = []
        for j in range(len(A[0])):
            tmp.append(A[i][j] + B[i][j])
        ans.append(tmp)
    return ans
