# Create Skipping inner iteration map
# Using prefix and suffix
def getPi(pattern):

    # When the first character of pattern doesn't match the character of target text,
    # the pointer has to move to first character of pattern.
    pi = [0]

    # While iterate pattern characters, 
    # find the longest set of characters that prefix and suffix are same.
    for i in range(int(len(pattern)) - 1):
        # sub-pattern(0~n)
        subp = pattern[:i+2]
        # If the length of sub-pattern is odd, compare character without center character.
        l = round(len(subp)/2-0.499)
        # Compare the prefix and the suffix of the subpattern until prefix and suffix are same.
        # If there is no case that prefix and suffix are same, skipping length is 0.
        while subp[:l] != subp[(l*-1):] or l == 0:
            l -= 1

        pi.append(l if l >= 0 else 0)
    
    return pi

# Find pattern in the text using KMP algorithm.
def patternSearch(text, pattern):
    # Create skipping inner iteration map.
    pi = getPi(pattern)
    
    result = []
    j = 0

    # Compare each character of text with certain character of pattern
    for i in range(len(text)):
        # Although the previous character already matches the previous character of pattern 
        # current character doesn't match the current character of pattern.
        # the pattern character point has to move previous position
        while j > 0 and text[i] != pattern[j]:
            j = pi[j-1]

        # If the current charactter matches the currenct character of pattern
        if text[i] == pattern[j]:
            # The character of pattern is last, the pointer has to move the previous postiion,
            # and append the current position in the result list
            if j == len(pattern)-1:
                result.append(i)
                j = pi[j]
            # It's not the last character, the pointer has to move next position
            else:
                j += 1

    return result