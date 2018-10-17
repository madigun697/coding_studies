import pmat_kmp
import pmat_aho_corasick
import pmat_baker_bird
import pmat_baker_bird_interleave

class KMP:
    def __init__(self, pattern, text):
        self._pattern = pattern
        self._text = text
        self.__result = pmat_kmp.patternSearch(self._text, self._pattern)

    def run(self):
        self.__result = pmat_kmp.patternSearch(self._text, self._pattern)

    def result(self):
        return self.__result

    def exist(self):
        return len(self.__result) > 0


class Aho_Corasick:
    def __init__(self, patterns, text):
        self._arr = patterns
        self._size = len(self._arr)
        self._text = text
        self.__result, _ = pmat_aho_corasick.patternSearch(self._arr, self._size, self._text)

    def run(self):
        self.__result, _ = pmat_aho_corasick.patternSearch(self._arr, self._size, self._text)

    def result(self, pattern):
        return self.__result[pattern]

    def exist(self):
        existCount = 0
        for p in self._arr:
            existCount += len(self.__result[p])
        return existCount
        
    def existPatterns(self):
        existPatterns = []
        for p in self._arr:
            if len(self.__result[p]) > 0:
                existPatterns.append(p)
        return ','.join(existPatterns)


class Baker_Bird:
    def __init__(self, pattern, origin):
        self._origin = origin
        self._pattern = pattern
        self.__result = pmat_baker_bird.patternSearch(self._origin, self._pattern)

    def result(self):
        return self.__result

    def exist(self):
        return len(self.__result) > 0
    
    
class Baker_Bird_Interleave:
    def __init__(self, pattern, origin):
        self._origin = origin
        self._pattern = pattern
        self.__result = pmat_baker_bird_interleave.patternSearch(self._origin, self._pattern)

    def result(self):
        return self.__result

    def exist(self):
        return len(self.__result) > 0    
    