class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ans = ""
        i = 0
        while len(ans) < len(s) and i < len(words):
            ans += words[i]
            i += 1
        return s == ans