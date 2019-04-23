n=input("Enter number:")
n=int(n)
n1=1
n2=1
if(n==1):
   print(n1,end='')
count=0
if(n>1):
  while(count==n-1):
     if(count==n-1):
        print(n1,end='')
     else:
        print(n1,end='')
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
