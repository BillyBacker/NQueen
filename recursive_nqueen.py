from itertools import permutations
import time
N = 10	
numSol = 0  			

b = N*[-1]  			
colFree = N*[1] 			
upFree = (2*N - 1)*[1] 		
downFree = (2*N - 1)*[1]    		

def printBoard(b):
    print(b)

def nqueen_recursive(r, b, colFree, upFree, downFree):
    global N
    global numSol
    for c in range(N): 
        if colFree[c] and upFree[r+c] and downFree[r-c+N-1]: 
            b[r] = c

            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0 

            if r == N-1:       
                printBoard(b)  
                numSol += 1
            else:
                nqueen_recursive(r+1, b, colFree, upFree, downFree)  
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1 

be = time.time()
nqueen_recursive(0, b, colFree, upFree, downFree)
print(time.time()-be)
