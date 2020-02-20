# pyth
#FIBONACI

import math



def fibo(n):
    f = []
    for i in range(n+1):
        if i <=1 :
            f.append(i)
        else : 
            f.append( f[i-1] + f[i-2])
            
    return (f[n])


def gcd(a,b): 
    best = 0 
    for d in range (1,(a+b)+1):
        if (a%d==0 and b%d ==0): 
            best = d
    return (best)
    
    
def eklides(a,b):
    
    if b == 0 : 
        return (a)
    else:
        return(eklides(b,a%b))
        
def lcm_naive(a, b):
    m = min(a,b)
    for i in range (2,m):
        if (a%i == 0 and b%i==0):
            return ((b*a)/i)
            break
        
def lcm(a,b): 
    m = max(a,b)
    l=1
    
    for i in range (2,m+1):
        if (a%i == 0 and b%i==0 ): 
            l=i
            break
    if l>1 : 
        return((a*b)/l)
    else : 
        return(a*b)
            
    