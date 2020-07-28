def ToString(list):
    return ''.join(list)

def ReverseString(text):
    return text[::-1]

def GetPosiblePermutations(text, permutationStructure, l, r):
    if(l==r):
        permutationStructure.append(ToString(text))
    else:
        for i in range(l, r+1):
            text[l],text[i] = text[i],text[l]
            GetPosiblePermutations(text, permutationStructure, l+1, r)
            text[l],text[i] = text[i],text[l]

def GetPalindromePermutations(text, length):
    text = ''.join(text.split())
    length = len(text)
    countDict = dict()

    # Create countDict to filter letter occurences
    for i in range(0,length):
        key = ord(text[i])
        if key in countDict:
            countDict[key] += 1
        else:
            countDict[key] = 1

    odd = 0
    oddChar = ""
    strHalfPal = ""

    # Find number of odd characters and last odd character
    for key in countDict:
        if(countDict[key]%2 != 0):
            odd+=1
            oddChar = key

    # Not a palindrome condition
    if(not((length%2 == 0 and odd == 0) or (length%2 == 1 and odd == 1))):
        print("Not a palindrome")

    # It is a palindrome
    else:
        # Create half palindrome without odd character
        for key in countDict:
            if(countDict[key]%2 == 0):
                strHalfPal += chr(key)

        # Find permutations of one half
        palPermutations = list()
        GetPosiblePermutations(list(strHalfPal), palPermutations, 0, len(strHalfPal)-1)
        
        # Fix first half + middle letter + last half
        for halfpal in palPermutations:
            print(halfpal + chr(oddChar) + ReverseString(halfpal))   

    

text = " r  ace car   "
GetPalindromePermutations(text, len(text))