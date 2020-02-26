#Uses python3

import sys
import numpy as np

def lcs2(a, b):
    #write your code here
    a1 =len(a)+1
    b1 = len(b)+1
    matreks = np.zeros((a1,b1))
    
    for i in range(0,a1-1): 
        for j in range(0,b1-1):
            if a[i]==b[j]:
                matreks[i+1][j+1]= matreks[i][j]+1
            else :
                matreks[i+1][j+1] = max(matreks[i][j+1] , matreks[i+1][j])
    
    
    return int( matreks[a1-1][b1-1])

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
