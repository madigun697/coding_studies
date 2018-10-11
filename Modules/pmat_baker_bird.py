import queue
import pmat_kmp
import pmat_aho_corasick

def test(t, p):
    patternSearch(t, p)
    print(pmat_aho_corasick.gotoMat)

def patternSearch(t, p):
    ta = []
    pa = []
    result = []

    for ti in list(map(list, zip(*t))):
        arr = list(reversed([''.join(pi) for pi in list(map(list, zip(*p)))]))
        text = ''.join(ti)
        k = len(arr)
        _, out = pmat_aho_corasick.patternSearch(arr, k, text)
        ta.append(out)

    for pi in list(map(list, zip(*p))):
        arr = list(reversed([''.join(pi) for pi in list(map(list, zip(*p)))]))
        text = ''.join(pi)
        k = len(arr)
        _, out = pmat_aho_corasick.patternSearch(arr, k, text)
        pa.append(out)
        
    for r, ti in enumerate(list(map(list, zip(*ta)))):
        
        text = ''.join([str(t) for t in ti])
        pattern = ''.join([str(p) for p in [o[-1] for o in pa]])
        
        kmp_result = pmat_kmp.patternSearch(text, pattern)
        sc = kmp_result[0] if len(kmp_result) > 0 else -1

        if sc >= 0:
            result.append([r - len(p) + 1, sc])

    return result