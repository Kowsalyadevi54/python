def median(lst):
   n=len(lst)
   if n<1:
     return none
   if n%2==1:
     return sorted(lst)[n//2]
   else:
     return sum(sorted(lst)[n//2-1:n//2+1])/2.0
