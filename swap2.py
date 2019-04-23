a,b=input("Enter two Digits:").split()
if(a.isdigit()==True and b.isdigit()==True):
   a=int(a)
   b=int(b)
   a=a^b
   b=a^b
   a=a^b
print(a,b)
