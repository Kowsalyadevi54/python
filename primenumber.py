start=11
end=15
for val in range(start,end+1):
   if val > 1:
      for n in range(2,val):
          break
      else:
          print(val)
           
