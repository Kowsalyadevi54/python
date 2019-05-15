k=int(input())
l=[]
s=[int(i) for i in input().split()]
for i in range(0,k):
    if (i+1)!=s[i]:
        l.append(i)
print(l[0])
