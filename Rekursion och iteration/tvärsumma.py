def tvärsumma(n):
  if n == 0:
    return 0
  else:
    return (n%10) + tvärsumma(n//10)
 
def tvärsumma2(n): # x //= 3 är samma som x = x // 3
    summa = 0
    while n:
        summa += n % 10
        n //= 10
    return summa


