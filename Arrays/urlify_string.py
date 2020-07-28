def UrlifyString(s, n):
    j = len(s)
    for i in range(n, 0, -1):
        if (j < 0):break

    if(s[i] != ' '):
        s[j] = s[i]
        j-=1
    else:
        s[j] = '0'
        j=-1
        s[j] = '2'
        j=-1
        s[j] = '%'
        j=-1

    return s

print(UrlifyString("Mr John Smith   ", 13))
