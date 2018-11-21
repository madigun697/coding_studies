def build_tables(patterns, m, b):
    shift_table = {}
    hash_table = {}

    for p in patterns:
        for q in range(1, m):
            shift_key = p[q-b+1:q+1]
            shift_table[shift_key] = min(shift_table[shift_key] if shift_key in shift_table.keys() else m-q-1, m-q-1)
            if shift_table[shift_key] == 0:
                hash_table[shift_key] = hash_table[shift_key] + [p] if shift_key in hash_table.keys() else [p]

    return shift_table, hash_table


def get_block_size(patterns, m):
    import math
    import itertools

    sigma_char = len(set(itertools.chain.from_iterable([list(p) for p in patterns])))
    return round(math.log((2*m*len(patterns)), sigma_char))


def patternSearch(text, patterns, block_size=0):
    output = dict(zip(patterns, [[] for i in patterns]))
    m = min([len(p) for p in patterns])
    b = block_size if block_size > 0 else get_block_size(patterns, m)
    max_shift = m-b+1

    shift_table, hash_table = build_tables(patterns, m, b)

    i = m-b
    while True:
        shift = shift_table[text[i:i+b]] if text[i:i+b] in shift_table.keys() else m-b+1
        
        if shift == 0:
            candidates = hash_table[text[i:i+b]]
            for c in candidates:
                if len(c) == m and c == text[i+b-m:i+b]:
                    output[c].append(i+b)
                elif c == text[i+b-m:i+b-m+len(c)]:
                    output[c].append(i+b+len(c)-m)
            i += 1
        else:
            i += shift

        if i >= len(text)-b+1:
            break

    return output