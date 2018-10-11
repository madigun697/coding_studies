def getPi(pattern):
    pi = [0]
    for i in range(int(len(pattern)) - 1):
        subp = pattern[:i+2]
        l = round(len(subp)/2-0.499)
        while subp[:l] != subp[(l*-1):] or l == 0:
            l -= 1
        pi.append(l if l >= 0 else 0)
    
    return pi

def patternSearch(text, pattern):
    pi = getPi(pattern)
    n = len(text)
    m = len(pattern)
    
    result = []
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j-1]

        if text[i] == pattern[j]:
            if j == m-1:
                result.append(i - m + 1)
                j = pi[j]
            else:
                j += 1

    return result