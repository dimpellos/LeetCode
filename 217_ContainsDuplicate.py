class Solution:
    def containsDuplicate(self, A: list[int]) -> bool:
        S = set(A)
        if len(A) != len(S):
            return True
        return False