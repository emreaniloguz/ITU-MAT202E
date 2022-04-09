import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def newton_poly(x,x_new,y):
    '''
    x: x-values
    x_new: x-value to be interpolated
    y: y-values
    '''

    n = len(y)
    coef = np.zeros([n, n])
    
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
    
    coef = coef[0,:]

    n = len(x) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x_new -x[n-k])*p
    return p


if __name__ == "__main__": 
    temperature = np.array([250,300,350,400,450,500])
    cp = np.array([1.003,1.005,1.008,1.013,1.020,1.029])
    cv = np.array([0.716,0.718,0.721,0.726,0.733,0.742])
    k = np.array([1.401,1.400,1.398,1.395,1.391,1.387])
    
    temperature_new = np.arange(250,501,10)
    cv_new= newton_poly(temperature,temperature_new,cv)
    cp_new = newton_poly(temperature, temperature_new, cp)
    k_new = newton_poly(temperature, temperature_new, k)

    
    table = np.array([temperature_new,cp_new,cv_new,k_new])

    print(tabulate(table.T, headers=["Temperature","Cp","Cv","K"]))


    fig,axs = plt.subplots(3,1,sharex=True)
    
    axs[0].plot(temperature, cp, 'o')
    axs[0].set_ylabel("Cp")
    axs[1].plot(temperature,cv,'o')
    axs[1].set_ylabel("Cv")
    axs[2].plot(temperature,k,'o')
    axs[2].set_ylabel("K")

    axs[0].plot(temperature_new, cp_new)
    axs[1].plot(temperature_new, cv_new)
    axs[2].plot(temperature_new, k_new)
    for i in range(3):
        axs[i].set_xlabel("Temperature")
        axs[i].legend()
        axs[i].grid()

    plt.show()