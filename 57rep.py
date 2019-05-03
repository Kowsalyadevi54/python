n,k=map(int,input().split())
sum=0
z=[int(i) for i in input().split()]
for i in range(0,n):
    if(k==z[i]):
       sum=sum+1
print(sum)
