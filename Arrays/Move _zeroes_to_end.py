def MoveZeroesToEnd(array, length):
    count = 0
    for i in range(0, length): 
        if (array[i] != 0): 
            array[count], array[i] = array[i], array[count] 
            count+=1

array = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
length = len(array)

MoveZeroesToEnd(array, length)

print(array)
