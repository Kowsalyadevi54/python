num=int(input("Enter any number:"))
flag=num%2
if flag==0:
  print(num,"Even number")
elif flag==1:
  print(num,"Odd number")
else:
  print("Invalid")
