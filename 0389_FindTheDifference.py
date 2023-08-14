class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = ord(t[-1])
        for i, ch in enumerate(s):
            ans ^= ord(ch) ^ ord(t[i])
        return chr(ans)
        # Plus 1 line solution
        # return chr(reduce(lambda x,y: x ^ y, map(ord,s+t)))