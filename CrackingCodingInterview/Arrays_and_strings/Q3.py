def ToString(list):
    return ''.join(list)

def CompressString_MyMethod(text):
    compressedString = list()
    length = len(text)

    occurence = 0
    for i in range(0,length):
        occurence+=1
        if(i+1 >= length or text[i] != text[i+1]):
            compressedString.append(text[i])
            compressedString.append(str(occurence))
            occurence=0    
        
    if(len(compressedString) == length):
        return text
    else:
        return ToString(compressedString)

text = "aaaabbcddddaa"
print(CompressString_MyMethod(text))
    