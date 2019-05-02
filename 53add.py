a=input()
b=0
for i in range(len(a)):
  if(a[i].isdigit()):
    b=b+int(a[i])
    print(b)
