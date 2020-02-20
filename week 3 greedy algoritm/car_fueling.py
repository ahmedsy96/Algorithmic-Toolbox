# python3
import sys


def compute_min_refills(distance, tank, stops,s):
    i =0 
    if (len(stops)==1):
        if (distance>tank):
            if ((stops[i]+m)>=distance):
               return(s+1) 
            else :
            
                return(-1)
        else : 
            return(s)
    elif (len(stops)==0): 
        if (m>=distance):
            return(0)
        else :
            return(-1)
    else: 
        if (stops[i]>tank):
            return(-1)
#        elif(tank==stops[i]):
#            tank = tank+m
        else :
            if (tank>stops[i]):
                if (stops[i+1]>tank): 
                    #tank = (tank-stops[i])+m
                    tank = stops[i]+m
                    s+=1
                    del stops[i]
                    return(compute_min_refills(distance, tank, stops,s))
                elif(stops[i+1]==tank):
                    tank = tank+m
                    del stops[i]
                    s+=1
                    return(compute_min_refills(distance, tank, stops,s))
                    
                else: 
                    del stops[i]
                    return(compute_min_refills(distance, tank, stops,s))
            elif(tank==stops[i]):
                s+=1
                tank = tank+m
                del stops[0]
                return(compute_min_refills(distance, tank, stops,s))
            else :
                return(-1)
                
                    
        
                
            
            
    
    
    
    
    
    #    if (i==len(stops)-1): 
#        return (s)
#        
#    else : 
#        if (len(stops)>1):
#            
#            if ((tank- stops[i])<(stops[i+1]-stops[i]))
    
    
    

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    
    s = 0
    stops = list(stops)
    print(compute_min_refills(d, m, stops,s))
