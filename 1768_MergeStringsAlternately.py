class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 1
        L = []
        if len(word1) > len(word2):
            L = list(word1)
            for ch in word2:
                L.insert(i, ch)
                i += 2
        else:
            L = list(word2)
            i -= 1
            for ch in word1:
                L.insert(i, ch)
                i += 2

        return "".join(str(x) for x in L)