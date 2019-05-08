str=input()
if(len(str)%2==0):
   k=len(str)//2
   print(str[:k-1]+'*'+str[k+1:])
else:
   k=len(str)//2
   print(str[:k]+'*'+str[k+1:])
