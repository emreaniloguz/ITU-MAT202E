from math import sin,cos,pi
from matplotlib import docstring
import matplotlib.pyplot as plt
import numpy as np
import random
from tabulate import tabulate


class Homework():
    def __init__(self):
        self.e = 2.71828182846

    def calculate_derivative(self,function,x):
        
        h = 1e-7
        top = function(x+h) - function(x)
        bottom = h
        slope = top/bottom

        return float("%.3f"%slope)

    def factorial(self,n):
        fact = 1
        for i in range(1,n+1):
            fact = fact*i

        return fact

    def ln(self,x):
        n = 1000.0
        return n * ((x ** (1/n)) - 1)


    def maclaurin_serie(self,x,n):
        '''
        param:: x = x value  ---> sin(0.3*pi) -> x=0.3*pi

        param:: n = significant figure variable ---> n= 8
        '''

        func_string = ""
        error_significant = (0.5 * 10**(2-n)) 
    
        previous_approximation  = 0
        print("n \t\t\t\t\t Result \t\t\t\t\t Ea")
        print("-------------------------------------------------------")
        for i in range(0,8,1):

                def f(x):
                    f = eval(func_string)
                    return f

                if i !=0:
                    previous_approximation = f(x)



                func_string += "+(" + str((-1)**i) +" * "  +"((x**" + str(1+(2*i)) +")"+ " / " + str(self.factorial(1+(2*i)))+ ")) " 


                
                current_approximation = f(x)

                approximation_error = abs((current_approximation - previous_approximation) / current_approximation)*100

                
                print(f"{i+1} \t\t\t\t\t {current_approximation} \t\t {approximation_error}")
                print("-------------------------------------------------------")

                if error_significant > approximation_error:
                    print(f"The root was found to be at {current_approximation} after {i+1} iterations, actual value is {sin(x)}")
                    break
       
        plt.plot(np.arange(-7,7,0.1),[f(x) for x in np.arange(-7,7,0.1)],label="Maclaurin serie")
        plt.plot(np.arange(-7,7,0.1),[sin(x) for x in np.arange(-7,7,0.1)],label="sin(x)",linestyle="--")
        plt.grid()
        plt.axhline(y=0, color='black', linestyle='-')
        plt.legend()
        plt.show()


    def bisection(self, function, xl, xu):

        '''
        :param function: function to be evaluated
        :param xl: lower bound
        :param xu: upper bound
        :return: root of the function
        '''


        first = xu
        significant = 0.05
        error = 0
        cnt=1
        table= []
        
        temp = 0 

        while True:
            
            
            xr = (xl+xu)/2


            plt.plot(np.arange(1,5,0.1),[f(x) for x in np.arange(1,5,0.1)],label="Bisection (1-->5)")
            plt.axhline(y=0, color='black', linestyle='-')
            plt.axvline(x=xl,color='red', linestyle='-',label="Xl")
            plt.axvline(x=xu,color='green', linestyle='-',label = "Xu")
            plt.axvline(x=xr,color='blue', linestyle='-', label = "Xr - Root")

            plt.legend()
            plt.grid()

            plt.close()


            if function(xl) * function(xu) >= 0 :
                print("Error")
                break

            elif function(xr) * function(xl) < 0:
                temp = xu
                xu = xr
                error = abs((xu-xl)/xu)*100
                table += [[cnt,xl,temp,xr,error]]
            elif function(xl) * function(xu) < 0:
                temp = xl
                xl = xr
                error = abs((xu-xl)/xl)*100
                table += [[cnt,temp,xu,xr,error]]

            if significant > error:
                print(f"The root was found to be at {xr} after {cnt} iterations\n\n")
                table = tabulate(table, headers=['Iteration', 'Xl', 'Xu','Xr','Ea (%)'], tablefmt='orgtbl')
                print(table)
                break
            
            cnt +=1
        


        return (xl+xu)/2

        


    def false_position(self, function, xl, xu):
        '''
        :param function: function to be evaluated
        :param xl: lower bound
        :param xu: upper bound
        '''

        cnt = 1
        c_before = 0



        c = (xl * function(xu)- xu * function(xl))/(function(xu)-function(xl)) #calculate the secant line 



        error = (abs(c-c_before)/c)*100
        error_significant = 0.05
        temp=0
        table = []
        

        while error > error_significant:


            xr = (xl * function(xu)- xu * function(xl))/(function(xu)-function(xl))

            if function(xl)*function(xu) >=0 :
                print("Error: The function does not change sign in the given interval, False-position method failed in this range")
                return  

            elif function(xr)* function(xl) <0:
                error = (abs(xr-xu)/xr)*100
                temp=xu
                xu = xr
                table += [[cnt,xl,temp,xr,error]]

            elif function(xr) * function(xu) <0 :
                error = (abs(xr- xl)/xr)*100
                temp = xl
                xl = xr
                table += [[cnt,temp,xu,xr,error]]
            
            else:
                print("Something wrong")
                return
            

            x = [xl,xu]
            y = [function(xl),function(xu)]
            plt.plot(np.arange(-7,7,0.1),[f(x) for x in np.arange(-7,7,0.1)],label="Function")
            plt.annotate(str(round(xu,5)),xy=(xu,function(xu)),xytext=(xu+0.005,function(xu)+0.005))
            plt.axvline(x=xl, color='black', linestyle='-')
            plt.axvline(x=xu, color='black', linestyle='-')
            plt.axhline(y=0,color="red",linestyle="-")

            plt.plot(x,y,label="Secant line")

            plt.close()


            
            cnt +=1

        print(f"The root was found to be at {xr} after {cnt-1} iterations\n\n")
        table = tabulate(table, headers=['Iteration', 'Xl', 'Xu','Xr','Ea (%)'], tablefmt='orgtbl')
        print(table)

    def newton_raphson(self,function, xi,number_of_steps):
        '''
        :param function: function to be evaluated
        :param xi: initial guess
        :param number_of_steps: number of iterations

        '''
        error_significant = 0.05
        error = 0
        table = []

        
        for i in range (1,number_of_steps):
            
            

            ix = xi - (function(xi)/self.calculate_derivative(function,xi)) 

            error = abs((ix-xi)/ix)*100

            table += [[i,xi,error]]

            if error_significant > error:
                print(f"The root was found to be at {ix} after {i} iterations\n\n")
                table = tabulate(table, headers=['Iteration', 'Xi', 'Ea (%)'], tablefmt='orgtbl')
                print(table)
                break

            plt.plot(np.arange(1,3,0.1),[function(x) for x in np.arange(1,3,0.1)],label="Function")
            plt.plot(xi,function(xi),'ro')
            slope_x = [ix, xi]
            slope_y = [0, function(xi)]
            plt.plot(slope_x,slope_y,label="Slope")
            plt.grid()
            plt.axhline(y=0, color='black', linestyle='-')
            plt.axvline(x=ix, color='black', linestyle='-',label = "X(i+1)")
            plt.legend()
            plt.show()

            xi = ix




        
        

    
    def secant_method(self,function, guess_1, guess_2,number_of_steps):
        '''
        :param function: function to be evaluated
        :param guess_1: initial guess
        :param guess_2: initial guess
        :param number_of_steps: number of iterations
        '''

        error_significant = 0.05
        table= []

        if guess_1 > guess_2:
            a = guess_1
            guess_1 = guess_2
            guess_2 = a


        for i in range(1,number_of_steps):


            xi = guess_1 - (function(guess_1)/((function(guess_1)-function(guess_2))/(guess_1-guess_2)))
            

            error = abs((xi-guess_2)/xi)*100
            table += [[i,xi,error]]


            if error_significant > error:
                print(f"The root was found to be at {xi} after {i} iterations\n\n")
                table = tabulate(table, headers=['Iteration', 'Xi', 'Ea (%)'], tablefmt='orgtbl')
                print(table)
                break

            guess_1 = guess_2
            guess_2 = xi



    
    def fixed_point_iteration(self,function,x0,number_of_steps):
        '''
        :param function: function to be evaluated
        :param x0: initial guess
        :param number_of_steps: number of iterations
        '''

        cnt = 1
        error = 1
        x0_list = []
        xi_list = []
        error_list = []
        error_significant = 0.05
        table = []

        for i in range(1,number_of_steps+1):
            xi = function(x0)


            xi_list.append(xi)


            error = (abs((xi-x0))/xi)*100

            table += [[i,xi,error]]

            x0_list.append(x0)


            x0 = xi
            
            cnt +=1

            error_list.append(error)
            
            if error_significant > error:
                print(f"The root was found to be at {xi} after {cnt-1} iterations\n\n")
                table = tabulate(table, headers=['Iteration', 'Xi', 'Ea (%)'], tablefmt='orgtbl')
                print(table)
                break


        plt.plot(error_list,xi_list,'blue')
        error_list =np.asarray(error_list)
        x0_list = np.asarray(x0_list)
        xi_list = np.asarray(xi_list)
        x= error_list
        y = xi_list
        plt.grid()
        plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale_units='xy',color="red" ,angles='xy', scale=1)

        plt.show()
        print(f"The root was found to be at {xi} after {number_of_steps} iterations")

        


if __name__ == "__main__":
    hw = Homework()

    ### Question 1
    
    #hw.maclaurin_serie(0.3*pi,8)

    ###  Question 2-A function
    
    f = lambda x: hw.ln(x) - cos(x) - hw.e**(-x)
    
    
    print(hw.bisection.__doc__)

    ### Question 2-A Methods

    #hw.trying(f,1,2)
    #hw.bisection(f,1,2)
    #hw.false_position(f,1,2)
    #hw.newton_raphson(f,random.uniform(1,2),10)
    #hw.secant_method(f,random.uniform(1,2),random.uniform(1,2),10)


    ### Question 2-B functions
    
    f_for_fixed = lambda x: hw.ln(x) - cos(x) - hw.e**(-x) + x
    f_for_fixed = lambda x: -hw.ln(x) + cos(x) + hw.e**(-x) + x
    
    ### Question 2-B Method
    
    #hw.fixed_point_iteration(f_for_fixed,1.5,120)



    #TODO: Implement table according to the hw assignment (DONE) 
    #TODO: Prepare Graphs instead of GIFs (DONE)
    #TODO: Make gifmaker.py function for the oop (CANCELLED)
    #TODO: Make errors as  described in the hw assignment (DONE)
    #TODO: Make the code more readable (DONE)
    #TODO: Make the code more efficient (DONE)
    #TODO: Publish on GitHub (DONE)