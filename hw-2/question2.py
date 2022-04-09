import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def gauss_elimination(A, b):

    temp_mat = np.c_[A, b] #combine A and b into one matrix
    
    n = temp_mat.shape[0] #number of rows

    #Loop over rows
    for i in range(n):
            
        p = np.abs(temp_mat[i:, i]).argmax() #pivot index
            
        p += i #pivot index with respect to original matrix 

        if p != i:                              #swap rows 
            temp_mat[[p, i]] = temp_mat[[i, p]]
            
        
        factor = temp_mat[i+1:, i] / temp_mat[i, i]             #Eliminate all entries below the pivot
        temp_mat[i+1:] -= factor[:, np.newaxis] * temp_mat[i]
                
  
    x = np.zeros_like(b, dtype=np.double);

    #Back substitution
    x[-1] = temp_mat[-1,-1] / temp_mat[-1, -2]
    
    for i in range(n-2, -1, -1):
        x[i] = (temp_mat[i,-1] - np.dot(temp_mat[i,i:-1], x[i:])) / temp_mat[i,i]    #Solve for each row
        
    return x

def fit_polynomials(x,y,degree):
    x_range = degree+4
    y_range = degree+1
    n = len(x)

    sum_x_list = []
    sum_y_list = []
    new_x  = np.zeros((y_range,y_range))
    new_y = np.zeros((y_range,1))

    for i in range(x_range):
        sum_x_list.append(np.sum(x**i))
    for i in range(y_range):
        sum_y_list.append(np.sum((x**i)*y))
    for i in range(y_range):
        try:
            new_x[i,0] = sum_x_list[i]
            new_x[i,1] = sum_x_list[i+1]
            new_x[i,2] = sum_x_list[i+2]
            new_x[i,3] = sum_x_list[i+3]
        except:
            pass
    for i in range(y_range):
        new_y[i,0] = sum_y_list[i]

    coefficients = gauss_elimination(new_x,new_y)
    
    
    if degree == 1:
        f = lambda x: coefficients[1][0]*x + coefficients[0][0]
    elif degree == 2:
        f = lambda x: coefficients[2][0]*x**2 + coefficients[1][0]*x + coefficients[0][0]
    elif degree == 3:
        f = lambda x: coefficients[3][0]*x**3 + coefficients[2][0]*x**2 + coefficients[1][0]*x + coefficients[0][0]

    plt.plot(np.arange(-0.1,2,0.01),[f(x) for x in np.arange(-0.1,2,0.01)],label=f"Order {degree} Fit",color="red")

    plt.legend()

    plt.scatter(x,y,s=10)
    plt.show()

    Sr = np.sum((y-f(x))**2)

    y_hat = np.sum(y)/n

    St = np.sum((y-y_hat)**2)

    r = np.sqrt((St-Sr)/St)
    table = np.array([[degree,Sr,St,r]])
    print(tabulate(table,headers=["Degree","Sr","St","r"]))


if __name__ == "__main__":

    x = np.array([-0.08782,0.084523,0.263619,0.293331,0.472033,
    0.529981,0.603711,0.783421,0.885681,0.914265,1.006573,1.070965,1.232576,
    1.359112,1.327033,1.477735,1.647759,1.75348,1.882376,1.813837,1.92543 ])

    y = np.array([0.078597,0.308436,0.62902,0.90405,0.880547,1.072706,1.081378,0.849039,
    0.669272, 0.449664,0.191648,-0.20313,-0.42675,-0.77451,-0.85954,-0.99787,-1.06124,
    -0.88792,-0.73878,-0.57943,-0.2393])


    for i in range(1,4):
        fit_polynomials(x,y,i)
