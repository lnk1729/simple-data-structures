def ReverseArray(array, start, end):
    while (start < end):
        array[start],array[end] = array[end],array[start]
        start+=1
        end-=1

def LeftRotate(array, rotations, length):
    if(rotations==0):
        return

    rotations = rotations % length
    ReverseArray(array, 0, rotations - 1)
    ReverseArray(array, rotations, length - 1)
    ReverseArray(array, 0, length - 1)

def RightRotate(array, rotations, length):
    if(rotations==0):
        return

    rotations = rotations % length
    ReverseArray(array, 0, length - 1)
    ReverseArray(array, 0, rotations - 1)
    ReverseArray(array, rotations, length - 1)
    
array = [1,2,3,4,5,6,7]
# LeftRotate(array, 3, len(array))
RightRotate(array, 9, len(array))
print(array)
    