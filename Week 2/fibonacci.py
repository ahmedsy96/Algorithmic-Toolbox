# Uses python3
def calc_fib(n):
    f = []
    s=0
    for i in range (n+1):
        if i<=1 :
            f.append(i)
            s= s+ f[i]
        else : 
            f.append( f[i-1]+f[i-2])
            s=s+f[i]
            

    return (s%10)

n = int(input())

print(calc_fib(n))
