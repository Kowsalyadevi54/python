str=input()
l=[]
for i in str:
    l.append(i)
k=set(l)
n=len(l)
m=len(k)
if n-m==0:
   print("yes")
else:
   print("No")
