N,K= [int(i) for i in input().split()]
if N>K:
  arr=[int(i) for i in input().split()]
  print(sum(arr[0:K]))
else:
  print("invalid")
