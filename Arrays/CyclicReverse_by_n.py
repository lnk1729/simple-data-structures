def CyclicReverse(array, rotCount, length):
    for i in range(rotCount):
        tmp = array[length - 1]
        for j in range(length -1, 0, -1):
            array[j] = array[j-1]
        array[0] = tmp
    return array

array = [1,2,3,4,5,6,7]
length = len(array)
rotCount = 2
print(CyclicReverse(array, rotCount, length))
    