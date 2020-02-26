# Uses python3
import numpy as np 
def edit_distance(s, t):
    #write your code here
    slist = list(s)
    tlist = list(t)
    s1 =len(slist)+1
    t1 = len(tlist)+1
    edit = np.zeros((s1,t1))
    for i in range (s1):
        edit[i][0]=i
    for j in range(t1):
        edit[0][j] = j

    
    for i in range(0,s1-1):
        for j in range (0,t1-1): 
            if slist[i] == tlist[j]:
                edit[i+1][j+1] = edit[i][j]
            else : 
                edit[i+1][j+1]= min(edit[i][j] , edit[i][j+1] , edit[i+1][j])+1 
#            print(edit)
#            print("****************")
                
    return int(edit[s1-1][t1-1])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
