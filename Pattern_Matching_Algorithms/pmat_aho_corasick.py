import queue

global MAXS # Sum of the length of patterns
MAXC = 27 # Count of Alphabet

# Making trie
def buildTrie(arr, size, gotoMat, fail, output, result):   
    state = 1
    
    # Iterate each pattern
    for i, word in enumerate(arr):
        result[word] = []
        presentState = 0

        # Iterate each character of pattern
        for c in word:
            # Using ascii, the character convert integer
            ch = ord(c) - ord('a') if ord(c) > 32 else 26

            # If go-to-matrix is empty(-1) then update
            if gotoMat[presentState][ch] == -1:
                gotoMat[presentState][ch] = state
                state = state + 1
            # Update previous state
            presentState = gotoMat[presentState][ch]

        # Update output table
        output[presentState] = output[presentState] | (1 << i)
                
    # Update root of go-to-matrix to 0
    for ch in range(MAXC):
        if gotoMat[0][ch] == -1:
            gotoMat[0][ch] = 0
            
    q = queue.Queue()
    
    # Update failure function table for first step(It's always 0)
    for ch in range(MAXC):
        if gotoMat[0][ch] != 0:
            fail[gotoMat[0][ch]] = 0
            q.put(gotoMat[0][ch])

    # Iterating trie, Update failure function
    while (q.qsize()):
        state = q.get()
        
        for ch in range(MAXC):
            if gotoMat[state][ch] != -1:
                failure = fail[state]
                # If failure function already exist then skip
                # It means that this pattern already calculated
                while gotoMat[failure][ch] == -1:
                    failure = fail[failure]
                failure = gotoMat[failure][ch]
                fail[gotoMat[state][ch]] = failure
                # Shifting output table value
                # If output already existed then the value is shifted,
                # If output doesn't exist(0) then the value is also 0.
                output[gotoMat[state][ch]] = output[gotoMat[state][ch]] | output[failure]
                q.put(gotoMat[state][ch])

    return state, gotoMat, fail, output, result


def getNextState(presentState, nextChar, gotoMat, fail):
    answer = presentState
    ch = ord(nextChar) - ord('a') if ord(nextChar) > 32 else 26
    
    # Move to other character of pattern using failure function
    while gotoMat[answer][ch] == -1:
        answer = fail[answer]
    
    return gotoMat[answer][ch]

# Find pattern in the text using Aho-corasick algorithm.
def patternSearch(arr, size, text):
    MAXS = sum([len(p) for p in arr]) + 1

    output = [0] * MAXS
    fail = [-1] * MAXS
    gotoMat = [[-1]*MAXC for _ in range(MAXS)]
    
    # Create Trie
    _, gotoMat, fail, output, result = buildTrie(arr, size, gotoMat, fail, output, dict())
    presentState = 0
    out = []
    
    # Iterate each character of input text
    for i, t in enumerate(text):
        # Update state
        presentState = getNextState(presentState, t, gotoMat, fail)
        out.append(presentState)

        # Output value is not 0, that means the subset of text and the any pattern among pattern list are same
        if output[presentState] != 0:
            # Find the pattern that match the subset of text
            for j in range(size+1):
                if output[presentState] & (1 << j):
                    result[arr[j]].append(i)
    
    return result, out