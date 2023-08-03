def factorial_iterative(n):
  ans=1
  for i in range (2,n+1):
    ans*=i
    return ans
def factorial_recurcive(n):
  if n==1 or n==0:
    return 1
  return n*factorial_recurcive(n-1)
    
    
