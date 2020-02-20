# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    f=[]
    for i in range(n+1):
        if i<=1 : 
            f.append(i)
        else : 
            f.append((f[i-1]+f[i-2])%10)
    return(f[n])

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)    
    print(get_fibonacci_last_digit_naive(n))
