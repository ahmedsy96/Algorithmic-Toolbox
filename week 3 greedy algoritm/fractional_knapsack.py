# Uses python3
import sys

def get_optimal_value(capacity, weights, values,vv,value):
    
    if(capacity==0):
        return value
    if (len(vv)==1 ): 
        if(weights[0]<=capacity):
            value = value+values[0]
            capacity = 0
        else :
            value = value + (vv[0]*capacity)
            capacity = 0
        return(get_optimal_value(capacity, weights, values,vv,value))
        
    
    if (weights[vv.index(max(vv)) ]>=capacity):
        value =value+ max(vv)*capacity
        capacity = 0
        return value
    else:
        
        value = value+ values[vv.index(max(vv)) ]
        capacity = capacity-weights[vv.index(max(vv)) ]
        values.pop(vv.index(max(vv)))
        weights.pop(vv.index(max(vv)))
        vv.pop(vv.index(max(vv)))
        return (get_optimal_value(capacity, weights, values,vv,value))
        
    
    
    
    
    

    


if __name__ == "__main__":
    value = 0
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    vv =  [i / j for i, j in zip(values, weights)]
    opt_value = get_optimal_value(capacity, weights, values ,vv,value)
    print("{:.10f}".format(opt_value))
