class lcm:
    def checkit(self,n,m):
        if n > m:
            greater = n
        else:
            greater = m
        while(True):
            if((greater % n==0) and (greater % m==0)):
                lcm=greater
                break
            greater+=1
        print(lcm)
n,m=map(int,input().split())
call=lcm()
call.checkit(n,m)
