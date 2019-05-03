import re
k=input()
if(re.findall('[a-z A-Z]',k)) and (re.findall('[0-9]',k)):
  print("yes")
else:
  print("no")
