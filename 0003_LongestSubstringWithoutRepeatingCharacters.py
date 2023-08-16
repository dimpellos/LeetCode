class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter, maxCounter = 0, 0
        d = {}
        for i, ch in enumerate(s):
            if ch in d:
                counter = min(i - d[ch], counter + 1)
            else:
                counter += 1
            d[ch] = i
            maxCounter = max(counter, maxCounter)

        return maxCounter