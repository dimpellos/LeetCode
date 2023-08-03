class Solution:
    def canJump(self, A: list[int]) -> bool:
        N = len(A)
        maxReach = 0
        for i in range(N):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + A[i])
        return True