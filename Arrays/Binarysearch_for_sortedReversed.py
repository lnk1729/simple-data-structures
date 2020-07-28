array = [4,5,6,7,1,2,3]
start = 0
end = len(array)-1
num = 2
found  = False

while start <= end:
    mid = (start + end)/2
    if(array[mid] == num):
        found = True
        break

    if(array[start] >= array[end]):
        if(num <= array[end]):
            start = mid+1
        else:
            end = mid-1
    else:
        if(num <= array[mid]):
            end = mid-1
        else:
            start = mid+1

if(found == True):
    print("Number {} found at position {}".format(num, mid))
else:
    print("Number not found")


