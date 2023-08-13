class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        A = sorted(set(nums))
        if len(A) < 3:
            return max(A)
        return A[-3]
