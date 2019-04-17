number=int(input("enter number:"))
if number>1:
   for i in range(2,number):
      if(number % i)==0:
          print(number,"yes")
          break
   else:
       print(number,"no")
