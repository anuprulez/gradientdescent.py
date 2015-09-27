# gradientdescent.py Gradient Descent Algorithm

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:51:53 2015

@author: anupkumar
"""

# Gradient descent with momentum #

from math import *
import numpy as np
import math
import matplotlib.pyplot as plt
import time

def calculate_gradient_descent():
    u = 800   
    e = 0.1
    meu = 0.5
    delta = 0
    #gradient_f = return_gradient(u)
    while return_gradient(u) != 0:
        delta = - e * return_gradient(u) + meu * delta
        u = u + delta
        print return_gradient(u) 
        cplot(u, return_function_value(u))


def return_function_value(u):
    f = (math.pow(u, 2)) - 100 * u - 100
    return f
    
    
def return_gradient(u):
     gradf = u - 100
     return gradf
    
    
def cplot(x, y): 
     plt.plot(x,y,'r.')  
     plot_function()
     plt.draw()
     plt.clf()  
    
    
def plot_function():  
    lx = []
    ly = []  
    input_values = np.arange(-1000,1000,0.1)
    for i in input_values:
        lx.append(i)
        ly.append(return_function_value(i))        
    plt.plot(lx,ly)
    plt.ion()
    plt.show()
    
    
calculate_gradient_descent()

