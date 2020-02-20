# Uses python3
import sys


       # choose the greater number
def lcm(a,b):
    return(int((a*b)/gcd_naive(a,b)))
    
        
        
def gcd_naive(a, b):
    if (b==0): 
        return a
    else : 
        return(gcd_naive(b,a%b))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())

    print(lcm(a, b))

