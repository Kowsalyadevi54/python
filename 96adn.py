a,d,n=map(int,input().split())
l=[]
y=1
for i in range(a,1000,d):
    if y <= n:
         l.append(i)
         y+=1
s=sum(l)
print(s)
