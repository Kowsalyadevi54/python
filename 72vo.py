import re
a=input()
if re.findall('[aeiou]',a):
   print('yes')
else:
   print('No')
