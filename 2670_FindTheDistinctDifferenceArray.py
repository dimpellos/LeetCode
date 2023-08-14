class Solution:
    def distinctDifferenceArray(self, A: list[int]) -> list[int]:
        diff = []
        for i in range(len(A)):
            diff.append(len(set(A[:i+1])) - len(set(A[i+1:])))
        return diff