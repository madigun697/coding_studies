def build_shift_dict(pattern):
    l = len(pattern)
    shift_dict = {}
    for i in range(l-1):
        shift_dict[pattern[i]] = l-i-1

    return shift_dict

def patternSearch(text, pattern):
    shift_dict = build_shift_dict(pattern)
    result = []
    l = len(pattern)
    i = 0

    while(i <= len(text)-l):

        shift = 0

        for j, t in enumerate(text[i:(l+i)][::-1]):
            if t != pattern[-j-1]:
                shift = shift_dict[t] if t in shift_dict.keys() else l
                break
            else:
                shift = 0

        if shift == 0:
            result.append(i)
            shift = 1

        if i == len(text)-l:
            break

        i = i + shift

    return result