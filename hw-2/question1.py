import numpy as np
from math import sqrt
from tabulate import tabulate

def print_matrix(Title, M):
    print(Title)
    for row in M:
        print([x for x in row])


def decompose_matrix(matrix):

    n = len(matrix)
    U = matrix.copy()
    L = np.eye(n, dtype=np.double) #Identity Matrix
    P = np.eye(n, dtype=np.double)
    for i in range(n):
        for k in range(i, n): 
            if ~np.isclose(U[i, i], 0.0): 
                break
            U[[k, k+1]] = U[[k+1, k]]
            P[[k, k+1]] = P[[k+1, k]]
    
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]


    return P, L, U

def forward_substitution(L, b):

    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double);

    y[0] = b[0] / L[0, 0]

    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]  
    return y


def back_substitution(U, y):
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double);
    x[-1] = y[-1] / U[-1, -1]

    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
    return x

def plu_inverse(A):
    n = len(A)
    b = np.eye(n)
    Ainv = np.zeros((n, n))
    P, L, U = decompose_matrix(A)
    for i in range(n):
        y = forward_substitution(L, np.dot(P, b[i, :]))
        Ainv[:, i] = back_substitution(U, y)
    return Ainv


def find_condition_number(A):
    """Finds the condition number of the matrix A, given the inverse matrix"""



    n = len(A)
    

    max_in_rows = np.amax(np.abs(A), axis=1) 
    max_in_normal = np.amax(A, axis=1)


    
    for i in range(n):          #Normalize matrix
        for j in range(n):
            if max_in_rows[i] == max_in_normal[i]:
                A[i][j] = A[i][j]/max_in_rows[i]    
            else:
                A[i][j] = A[i][j]/-max_in_rows[i] 

    max_in_rows =np.amax(np.abs(A).sum(axis=1)) #Find max in  rows with sum of abs
    A_inv = plu_inverse(np.array(A))

    max_in_inv_rows = np.amax(np.abs(A_inv).sum(axis=1))
    

    cond_A = max_in_inv_rows*max_in_rows
    print("Condition number of A: ", cond_A)



def transpose(L):
    """Transposes a lower triangular matrix L."""
    n = len(L)
    LT = [[0.0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            LT[j][i] = L[i][j]
    return LT


def cholesky(A):
    '''
    Cholesky decomposition of a positive definite matrix A.
    Returns the lower triangular matrix L such that A = L*LT.
    '''


    n = len(A)

    L = [[0.0] * n for i in range(n)]

    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k)) 
            
            if (i == k):
                L[i][k] = sqrt(A[i][i] - tmp_sum)   
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum)) 
    U = transpose(L)
    return L,U


      





if __name__ == "__main__":
    
    matrix = [[87.82557,0.0,-43.91278,3659.399,0.0,0.0],
              [0.0,813199.7,-3659.399,203299.9,0.0,0.0],
              [-43.91278,-3659.399,87.82557,0.0,-43.91278,3659.399],
              [3659.399,203299.9,0,813199.7,-3659.399,203299.9],
              [0.0,0.0,-43.91278,-3659.399,44.41278,-3659.399],
              [0.0,0.0,3659.399,203299.9,-3659.399,406599.8]]
    
    
    ## Question 1-A)
    #P,L,U = decompose_matrix(np.array(matrix))
    #print_matrix("L", L)
    #print_matrix("U", U)

    
    ## Question 1-B)
    #L,U = cholesky(matrix)
    #print_matrix("L", L)
    #print_matrix("U", U)

    ## Question 1-C)
    #A_Inv = plu_inverse(np.array(matrix))
    #print_matrix("A_Inv", A_Inv)

    ## Question 1-D)
    #find_condition_number(np.array(matrix))



