class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = len(columnTitle)
        ans = 0
        for ch in columnTitle:
            ans += (ord(ch) - ord('A') + 1) * (26**(l-1))
            l -= 1

        return ans 
