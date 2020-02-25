# Uses python3
import sys

def get_change(m):
    #write your code here
    if m == 1 or m==2 : 
        return m 
    elif m == 3 :
        return 1 
    else : 
        
        if m % 4 > 0 : 
            return (m//4)+1
        
        else : 
            
        
             return m // 4

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
