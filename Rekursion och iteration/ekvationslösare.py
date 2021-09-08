import math

def derivative(f,x,h):
    return (1/(2 * h)) * (f(x+h) - f(x-h))    

derivative(math.sin, math.pi, 0.0001)

"""def solve(f,x0,h):

 x - f(x)/derivative(f(x))"""
        

