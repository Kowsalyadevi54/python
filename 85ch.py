s=input()
o,e="",""
for i in range(len(s)):
     if i%2:
         o+=s[i]
     else:
         e+=s[i]
print(e,o)
