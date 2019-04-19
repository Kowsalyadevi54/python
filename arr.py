z=int(input())
lis=[int(i) for i in input().split()]
lis1=sorted(lis)
for i in range(0,len(lis1)-1):
     print(lis1[i],end="")
     print(lis1[-1])
