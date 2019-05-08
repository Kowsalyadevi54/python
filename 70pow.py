import math
n1=int(input())
for i in range(n1):
    if 2**i==n1:
       k=i
       break
print(2**(k+1))
