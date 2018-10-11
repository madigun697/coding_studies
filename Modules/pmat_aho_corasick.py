import queue

MAXS = 500
MAXC = 26

def buildTree(arr, size, gotoMat, fail, output, result):   
    state = 1
    
    for i, word in enumerate(arr):
        result[word] = []
        presentState = 0

        for c in word:
            ch = ord(c) - ord('a')
            if gotoMat[presentState][ch] == -1:
                gotoMat[presentState][ch] = state
                state = state + 1
            presentState = gotoMat[presentState][ch]

        output[presentState] = output[presentState] | (1 << i)
                
    for ch in range(MAXC):
        if gotoMat[0][ch] == -1:
            gotoMat[0][ch] = 0
            
    q = queue.Queue()
    
    for ch in range(MAXC):
        if gotoMat[0][ch] != 0:
            fail[gotoMat[0][ch]] = 0
            q.put(gotoMat[0][ch])

    while (q.qsize()):
        state = q.get()
        
        for ch in range(MAXC):
            if gotoMat[state][ch] != -1:
                failure = fail[state]
                while gotoMat[failure][ch] == -1:
                    failure = fail[failure]
                failure = gotoMat[failure][ch]
                fail[gotoMat[state][ch]] = failure
                output[gotoMat[state][ch]] = output[gotoMat[state][ch]] | output[failure]
                q.put(gotoMat[state][ch])

    return state, gotoMat, fail, output, result


def getNextState(presentState, nextChar, gotoMat, fail):
    answer = presentState
    ch = ord(nextChar) - ord('a')
    
    while gotoMat[answer][ch] == -1:
        answer = fail[answer]
    
    return gotoMat[answer][ch]


def patternSearch(arr, size, text):
    output = [0] * MAXS
    fail = [-1] * MAXS
    gotoMat = [[-1]*MAXC for _ in range(MAXS)]
    
    _, gotoMat, fail, output, result = buildTree(arr, size, gotoMat, fail, output, dict())
    presentState = 0
    out = []
    
    for i, t in enumerate(text):
        presentState = getNextState(presentState, t, gotoMat, fail)
        out.append(presentState)
        if output[presentState] != 0:
            for j in range(size+1):
                if output[presentState] & (1 << j):
                    result[arr[j]].append(i - len(arr[j]) + 1)
    
    return result, out


if __name__ == '__main__':
    print('start')