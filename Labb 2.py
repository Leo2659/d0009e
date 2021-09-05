import math

def bounce(n):
    print(n)

    if(n>0):
        bounce(n-1)
        print(n)

def bounce2(n):
    for x in range(-n, n+1):
        print(abs(x))
   

