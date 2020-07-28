def StringCharsUnique(stringName):
    stringName = sorted(stringName)
    for i in range(0,len(stringName) - 1):
        if(stringName[i] == stringName[i + 1] ):
            return False
    return True

stringName = "Prathiksh"
print(StringCharsUnique(stringName))

#O(nlogn)