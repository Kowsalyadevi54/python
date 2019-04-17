N,Q=map(int,input().split())
for i in range(N+1,Q):
   if i % 2!=0:
      if i!=Q-1:
         print(i,end='')
   else:
       print(i,end='')
