class Solution:
    def lengthOfLastWord(self, S: str) -> int:
        return len(S.strip().split(' ')[-1])