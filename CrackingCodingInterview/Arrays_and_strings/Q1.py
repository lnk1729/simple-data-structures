def ToString(list):
    return ''.join(list)

def GetAllPermutations(text, l, r):
    if(l==r):
        print(ToString(text))
    else:
        for i in range(l, r+1):
            text[l],text[i] = text[i],text[l]
            GetAllPermutations(text, l+1, r)
            text[l],text[i] = text[i],text[l]

text = "ABCD"
GetAllPermutations(list(text), 0 , len(text) - 1)
