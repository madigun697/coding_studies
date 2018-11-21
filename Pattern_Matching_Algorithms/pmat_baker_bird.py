import queue
import pmat_kmp # Using KMP algorithm
import pmat_aho_corasick # Using Aho-corasick algorithm

def patternSearch(t, p):

    result = []
    # Create pattern for KMP
    kmpp = ''.join([str(pmat_aho_corasick.patternSearch(p, len(p), pi)[1][-1]) for pi in p])
    kmpt = []

    # Run aho corasick matching by each row
    for text in t:
        kmpt.append(''.join([str(ti) for ti in pmat_aho_corasick.patternSearch(p, len(p), text)[1]]))

    # Iterate Each aho corasick matching results of each row  
    for col_idx in range(len(kmpt)):
        text = ''.join([ti[col_idx] for ti in kmpt])
        # Run KMP
        # Pattern is aho corasick matching results of pattern matrix
        kmp_result = pmat_kmp.patternSearch(text, kmpp)
        if len(kmp_result) > 0:
            for row_idx in kmp_result:
                result.append((row_idx, col_idx))

    return result