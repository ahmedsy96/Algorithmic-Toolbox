# Uses python3
import sys
    
        

    


def get_majority_element(a):
    a.sort()
    count=1
    prev= a[0] 
    for i in range(1,len(a)):
        if a[i]==prev: 
            count+=1 
        else : 
            count = 1
            prev = a[i]
        
        if count> len(a)/2:
            return 1
            break
            
        
        

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) == 1:
        print(1)
    else:
        print(0)
        
