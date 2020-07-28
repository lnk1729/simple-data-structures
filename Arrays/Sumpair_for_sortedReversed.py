def FindSumPairs(sum, array, n):
    array_of_pairs = []
    i=0
    for i in range(0,n-1):
        if(array[i] > array[i+1]):
            break

    i_smallest = (i + 1) % n
    i_largest = i


    while (i_smallest != i_largest):
        if(array[i_largest] + array[i_smallest] == sum):
            array_of_pairs.append([array[i_largest],array[i_smallest]])
    
            if(i_smallest == (i_largest - 1 + n) % n):           
                return array_of_pairs

            i_smallest = (i_smallest+1) % n
            i_largest = (i_largest -1 + n) % n

        elif(array[i_largest] + array[i_smallest] > sum):
            i_largest =  (i_largest -1 + n) % n

        else:
            i_smallest = (i_smallest+1) % n        
    
    return array_of_pairs
        
    


array = [1,2,3,4,5,6,7,8]
sum = 8
n = len(array)

print(FindSumPairs(sum, array, n))