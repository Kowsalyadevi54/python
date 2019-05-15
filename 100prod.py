n=int(input())
pro=1
k=0
while(n):
    k=n%10
    pro=pro*k
    n=n//10
print(pro)
