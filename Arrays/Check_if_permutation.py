def CheckIfPermutation_Method1(s1, s2):
    if(len(s1) != len(s2)):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if(s1[i] != s2[i]):
            return False

    return True

def CheckIfPermutation_Method2(s1, s2):
    count = []
    if(len(s1) != len(s2)):return False

    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1

    if(len(count)):return False

    return True
    
s1 = "racecar"
s2 = "carrace"
print(CheckIfPermutation_Method2(s1, s2))
    
