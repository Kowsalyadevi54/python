str=input()
l=[]
for i in range(0,len(str)):
    l.append(ord(str[i]))
l.sort()
for i in l:
    print(chr(i),end=' ')
