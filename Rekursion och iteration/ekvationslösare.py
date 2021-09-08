import math

def derivative(f,x,h):
    return (1/(2*h)*(f*(x+h)-f*(x-h))) 
