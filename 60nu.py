num=int(input("enter value:"))
hold=num
sum=0
if num<=0:
   print("Enter a positive value:")
else:
   while num>0:
      sum=sum+num
      num=num-1
      print("sum of first",hold,"natural num is:",sum)
