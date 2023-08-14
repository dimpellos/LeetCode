class Solution:
    def rob(self, A: list[int]) -> int:
        dp1 = dp2 = 0
        for num in A:
            dp2, dp1 = dp1, max(dp1, dp2 + num)
        return dp1