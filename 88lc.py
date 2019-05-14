x1,y=map(int,raw_input().split())
if x1>y:
    greater=x1
else:
    greater=y
while(True):
    if((greater % x1==0) and (greater % y==0)):
        lcm=greater
        break
    greater=greater+1
print(lcm)
