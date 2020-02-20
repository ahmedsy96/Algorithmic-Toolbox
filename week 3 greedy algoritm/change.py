# Uses python3
import sys

def get_change(m,s):
    if (m==0) : 
        return s
    
    if (m>= 10): 
        s= int(m/10)
        m=m%10
        return(get_change(m,s))
    elif(5<=m<10):
        s = s+1
        m=m%5
        return(get_change(m,s))
    else : 
        s=s+m
        m=0
        return(get_change(m,s))
        
        
        
        
    

if __name__ == '__main__':
    s=0
    m = int(sys.stdin.read())
    print(get_change(m,s))
