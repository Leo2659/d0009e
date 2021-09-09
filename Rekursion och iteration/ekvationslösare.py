import math


def derivative(f,x,h):
    return (1/(2 * h)) * (f(x+h) - f(x-h))    

def f(x):
    return x**2+1

def solve(f,x0,h):
    running = True
    while running:
        x1 = x0 - (f(x0)/derivative(f,x0,h))
        if abs(x0-x1) < h:
            return x1
        else:
            x0 = x1

import d0009e_lab2_solveTest
        

