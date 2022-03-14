from math import sin,cos,pi
from tkinter import X
import matplotlib.pyplot as plt
import numpy as np
import random

from torch import rand

class Plotify():
    def __init__(self):
        pass


    def plot_sin(self,x,y):
        plt.plot(x,y)
        plt.show()




class Homework():
    def __init__(self):
        self.e = 2.71828182846
        self.error_acceptable = 5* 1e-4
        self.plotter = Plotify()


    def calculate_derivative(self,function,x):
        
        h = 1e-7
        top = function(x+h) - function(x)
        bottom = h
        slope = top/bottom

        return float("%.3f"%slope)

    def maclaurin_serie(self,function,x,n):
       
        #x = pi/180
        sum_list = []
        sum = 0
        sum += x
        if n == 0:
            return function(x)
        else:
            for i in range(1,n+1):
                print("Sum {} at step {}".format(sum,i))
                if i%2 == 0:
                    
                    sum += (x**(i+2))/self.factorial(i+2) 
                else :
                    sum -= (x**(i+2))/self.factorial(i+2)
                sum_list.append(sum)



            plt.plot(range(1,9),sum_list,label="Maclaurin serie")
            plt.plot(range(1,9),[sin(x) for x in range(1,9)],label="sin(x)")
            plt.plot(range(1,9),sum_list,"ro",label="Approximation")
            plt.legend()
            plt.show()
               
            print("Maclaurin: ",sum)

    def factorial(self,n):
        fact = 1
        for i in range(1,n+1):
            fact = fact*i
        #print(fact)
        return fact

    def ln(self,x):
        n = 1000.0
        return n * ((x ** (1/n)) - 1)

    def bisection(self, function, interval_a, interval_b):
        cnt = 1
        error = abs(interval_b - interval_a)
        mid_point_list = []
        error_list = []
        error_list.append(error)
        if function(interval_a)*function(interval_b) >= 0:
            print("Error: The function does not change sign in the given interval")
            return
        else:
            a_n = interval_a
            b_n = interval_b
            while error > self.error_acceptable:
                midpoint = (a_n+b_n)/2
                mid_point_list.append(midpoint)

                function_midpoint = function(midpoint)

                if function(a_n)*function_midpoint < 0:
                    a_n = a_n
                    b_n = midpoint
                    error = abs(b_n-a_n)
                    error_list.append(error)

                elif function(b_n)*function_midpoint < 0:
                    a_n = midpoint
                    interval_b = b_n
                    error = abs(b_n-a_n)
                    error_list.append(error)

                elif function_midpoint ==0:
                    print("Root found at: ",midpoint)
                    return midpoint
                else:
                    print("Bisection failed")
                    return
                cnt += 1

            print("Approximate root of the eq, using Bisection Methed is: ",str(midpoint) + " After ",str(cnt)," steps")
            plt.plot(range(1,cnt),[function(i) for i in range(1,cnt)],label="Function")
            plt.scatter((a_n+b_n)/2,function((a_n+b_n)/2),label="Root")
            #plt.plot(range(1,cnt),[error_list[i] for i in range(1,cnt)],label="Error",color="red")

            for i in range(cnt-1):
                col = [np.random.random(), np.random.random(), np.random.random()]

                plt.scatter(mid_point_list[i],function(mid_point_list[i]),label="Step : "+ str(i+1) +" ->> " +str(round(mid_point_list[i],3)),color=col)
                #plt.annotate(str(mid_point_list[i]),xy=(mid_point_list[i],function(mid_point_list[i])),xytext=(mid_point_list[i]+0.005,function(mid_point_list[i])+0.005))
            
            plt.axhline(y=0, color='black', linestyle='-')
            plt.grid()
            plt.legend()
            plt.show()
            plt.close()
            plt.plot(range(1,cnt),[error_list[i] for i in range(1,cnt)],label="Error",color="red")
            for i in range(cnt-1):
                #plt.scatter(mid_point_list[i],error_list[i],label="Step : "+ str(i+1) +" ->> " +str(round(mid_point_list[i],3)),color="red")
                error_list[i] = round(error_list[i],3)
                plt.scatter(i,error_list[i])
                plt.annotate(str(error_list[i]),xy=(i,error_list[i]),xytext=(i+0.005,error_list[i]+0.005))
            plt.show()
            return (a_n+b_n)/2

    def false_position(self, function, interval_a, interval_b):

        cnt = 1
        c_before = 0
        c = (interval_a * function(interval_b)- interval_b * function(interval_a))/(function(interval_b)-function(interval_a)) #calculate the secant line 
        error = abs(c-c_before)
        c_after_list = []
        error_list = []
        

        while error > self.error_acceptable:
            c_after = (interval_a * function(interval_b)- interval_b * function(interval_a))/(function(interval_b)-function(interval_a))
            c_after_list.append(c_after)

            if function(interval_a)*function(interval_b) >=0 :
                print("Error: The function does not change sign in the given interval, False-position method failed in this range")
                return  

            elif function(c_after)* function(interval_a) <0:
                error = abs(c_after-interval_b)
                interval_b = c_after


            elif function(c_after) * function(interval_b) <0 :
                error = abs(c_after- interval_a)
                interval_a = c_after
            
            else:
                print("Something wrong")
                return
            
            #plt.plot(range(1,cnt),[function(i) for i in range(1,cnt)],label="Function")
            x = [interval_a,interval_b]
            y = [function(interval_a),function(interval_b)]
            plt.plot(range(1,5),[function(i) for i in range(1,5)],label="Function in 10 steps")
            plt.annotate(str(round(interval_b,5)),xy=(interval_b,function(interval_b)),xytext=(interval_b+0.005,function(interval_b)+0.005))
            plt.axvline(x=interval_a, color='black', linestyle='-')
            plt.axvline(x=interval_b, color='black', linestyle='-')
            plt.axhline(y=0,color="red",linestyle="-")
            #plt.plot(function(interval_a),function(interval_b),label="Secant line")
            plt.plot(x,y,label="Secant line")
            plt.show()


            print(f"The error remainig is {error}, after {cnt} iteration")
            print(f"The root can be approximately found at {c_after}")
            print(f"The lower root boundary, interval_a, is {interval_a}, the upper root boundary, interval_b, is {interval_b}")
            
            cnt +=1


    def newton_raphson(self,function, initial_guess,number_of_steps):

        for i in range (1,number_of_steps):

            print(initial_guess)
            ix = initial_guess - (function(initial_guess)/self.calculate_derivative(function,initial_guess)) 
            plt.plot(range(1,number_of_steps),[function(i) for i in range(1,number_of_steps)],label=f"Function in {number_of_steps} steps")
            if i == 1:
                plt.plot(initial_guess, function(initial_guess), 'ro', label='Initial guess')
            else:
                plt.plot(initial_guess, function(initial_guess), 'ro')

            plt.axvline(x=initial_guess, color='red', linestyle='-')
            plt.axhline(y=0, color='black', linestyle='-')
            plt.annotate(str(initial_guess),xy=(initial_guess,function(initial_guess)),xytext=(initial_guess+0.2,function(initial_guess)+0.2))
            plt.legend()
            plt.savefig(f"newton_gif/Newton_raphson_method_in_{i}_steps.png")
            plt.clf()
            #plt.show()
            initial_guess = ix


        
        print(f"The root was found to be at {initial_guess} after {number_of_steps} iterations")

    
    def secant_method(self,function, guess_1, guess_2,number_of_steps):

        if guess_1 > guess_2:
            a = guess_1
            guess_1 = guess_2
            guess_2 = a


        for i in range(1,number_of_steps):

            if self.error_acceptable > abs(guess_2 - guess_1):
                print(f"The error is {abs(guess_2 - guess_1)}")
                print(f"The root can be approximated at {guess_2}")
                return

            xi = guess_1 - (function(guess_1)/((function(guess_1)-function(guess_2))/(guess_1-guess_2)))

            plt.plot(range(1,number_of_steps),[function(i) for i in range(1,number_of_steps)],label=f"Function in {number_of_steps} steps")
            
            x = [guess_1,guess_2]
            y = [function(guess_1),function(guess_2)]
            plt.axvline(x=guess_1, color='red', linestyle='-')
            plt.axvline(x=guess_2, color='red', linestyle='-')
            plt.axhline(y=0, color='black', linestyle='-')
            plt.plot(xi, function(xi), 'ro', label='Root')
            plt.plot(x,y,label="Secant line",color="red")
            plt.plot(guess_1,function(guess_1),'bo',label="Initial guess 1")
            plt.plot(guess_2,function(guess_2),'go',label="Initial guess 2")
            plt.annotate(str(xi),xy=(xi,function(xi)),xytext=(xi+0.2,function(xi)+0.2))
            plt.legend()
            plt.savefig(f"secant_gif/Secant_method_in_{i}_steps.png")
            
            #plt.show()
            plt.clf()

            guess_1 = guess_2
            guess_2 = xi

        print(f"The root was found to be at {xi} after {number_of_steps} iterations")

    
    def fixed_point_iteration(self,function,x0,number_of_steps):

        cnt = 1
        error = 1
        while error> self.error_acceptable and cnt < number_of_steps:
            xi = function(x0)
            x0 = xi
            error = abs(x0-xi)
            cnt +=1

        print(f"The root was found to be at {xi} after {number_of_steps} iterations")


if __name__ == "__main__":
    hw = Homework()
    #hw.calculate_derivative(lambda x: x**3,1)
    #hw.factorial(5)
    #abo=hw.maclaurin_serie(lambda x: sin(x),0.3*pi,8)

    f = lambda x: hw.ln(x) - cos(x) - hw.e**(-x)
    f_for_fixed = lambda x: hw.ln(x) - cos(x) - hw.e**(-x) + x
    f_for_fixed = lambda x: -hw.ln(x) + cos(x) + hw.e**(-x) + x

    hw.bisection(f,1,2)
    #hw.false_position(f,1,2)
    #hw.newton_raphson(f,random.uniform(1,2),10)
    #hw.secant_method(f,random.uniform(1,2),random.uniform(1,2),10)
    #hw.fixed_point_iteration(f_for_fixed,1.5,50)



    #TODO: Implement table according to the hw assignment
    #TODO: Prepare Graphs instead of GIFs
    #TODO: Make gifmaker.py function for the oop
    #TODO: Make errors as  described in the hw assignment
    #TODO: Make the code more readable
    #TODO: Make the code more efficient
    #TODO: Publish on GitHub