def RotateArray(array, rotCount, length):
    for i in range(rotCount):
        tmp = array[0]
        for j in range(length - 1):
            array[j] = array[j+1]
        array[length - 1] = tmp
    return array
            
    

array = [1,2,3,4,5,6,7]
length = len(array)
rotCount = 2
print(RotateArray(array, rotCount, length)) 
