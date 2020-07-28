import numpy as np
import math as math

def ReArrange(array, length):
    tmpArr = np.zeros(length, dtype=int)    
    evenPos =  int(math.ceil(length/2))-1
    array.sort() 

    start=0
    for i in range(evenPos, -1, -1):        
        tmpArr[start] = array[i]
        start+=2

    start=1
    for i in range(evenPos+1, length):
        tmpArr[start] = array[i]
        start+=2

    return tmpArr

array = [1,2,1,4,5,6,8,8]
print(ReArrange(array, len(array)))
