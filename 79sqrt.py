import math
k,v=map(int,input().split())
l=math.sqrt(k*v)
if(l-int(l)==.0):
   print("yes")
else:
   print("no")
   
