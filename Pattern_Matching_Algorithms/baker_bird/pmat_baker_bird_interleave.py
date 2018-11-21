import queue
import pmat_kmp # Using KMP algorithm
import pmat_aho_corasick # Using Aho-corasick algorithm

def patternSearch(t, p):
    result = []

    # Create KMP Pointer list
    js = [0] * len(t[0])
    # Create pattern for KMP
    kmpp = ''.join([str(chr(pmat_aho_corasick.patternSearch(p, len(p), pi)[1][-1] + ord('a'))) for pi in p])
    # Create Skipping inner iteration map for KMP
    pi = pmat_kmp.getPi(kmpp)

    # Iterate each row
    for row_idx, text in enumerate(t):
        # Create text using aho corasick matching results of each row
        kmpt = ''.join([str(chr(ti + ord('a'))) for ti in pmat_aho_corasick.patternSearch(p, len(p), text)[1]])

        # Run KMP algorithm's single step
        # Pattern is aho corasick matching results of pattern matrix
        # Text is aho corasick matching results of each row
        for col_idx, text2 in enumerate(kmpt):
            while js[col_idx] > 0 and text2 != kmpp[js[col_idx]]:
                js[col_idx] = pi[js[col_idx] - 1]

            if text2 == kmpp[js[col_idx]]:
                if js[col_idx] == len(kmpp) - 1:
                    result.append((row_idx, col_idx))
                    js[col_idx] = pi[js[col_idx]]
                else:
                    js[col_idx] += 1

    return result