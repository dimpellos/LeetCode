class Solution:
    def romanToInt(self, s: str) -> int:
        matches = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num, i, N = 0, 0, len(s)
        while i < N:
            if i != (N-1) and matches[s[i]] < matches[s[i+1]]:
                num += matches[s[i+1]] - matches[s[i]]
                i += 2
            else:
                num += matches[s[i]]
                i += 1 
        
        return num
