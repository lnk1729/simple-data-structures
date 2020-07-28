def RotateArrayWithCount(array, length, k):
    for i in range(k,k+length):
        print(str(array[i%length]) + " ")

array = [1,2,3,4,5]
RotateArrayWithCount(array, len(array), 2)