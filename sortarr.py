n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
for i in range(0,len(k)):
   if i==len(k)-1:
      print(k[i])
   else:
      print(k[i],end="")
