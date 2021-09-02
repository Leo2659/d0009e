import math
def bounce(n):
    if(n >= 0):
        for x in reversed(range(0,n+1)):
            print(x)
        for x in range(1,n+1):
            print(x)
    else:
        print("Bounce finns inte för anviget tal")

def tvärsumma(n):
    if n > 0:
        n = n % 10 + tvärsumma(n/10)
    return n