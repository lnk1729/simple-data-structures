def GetMaxIndexElemProductSummation(arr, length):
    maxSum = 0
    rotations = 0

    offSet = 0
    for i in range(0, length):
        rotationMaxSum = 0
        for j in range(0,length):
            rotationMaxSum += j*arr[(j+offSet)%length]
        offSet+=1
        if(rotationMaxSum > maxSum):
            maxSum = rotationMaxSum
            rotations = i+1

    return [maxSum, rotations]





arr = [1,20,2,10]
length = len(arr)
result = GetMaxIndexElemProductSummation(arr, length)
print("Max product summation = {} for {} rotations".format(result[0],result[1]))