k=int(input())
sum=0
for i in range(2,k//2):
    if k%i==0:
       sum=sum+1
if(sum>0):
   print("yes")
else:
   print("No")
   
       
