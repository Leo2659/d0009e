from Sockerkaka import recept
import math

def bounce(n):
    if(n==0):
        print(n)
        return bounce(n+1)
    else:
        print(n)
        return bounce(n-1)


def bounce2(n):
    if(n >= 0):
        for x in reversed(range(0, n+1)):
            print(x)
        for x in range(1, n+1):
            print(x)
    else:
        print("Testa igen med ett heltal >= 0")


