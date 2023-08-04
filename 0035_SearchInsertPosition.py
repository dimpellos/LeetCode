class Solution:
    def searchInsert(self, A: list[int], target: int) -> int:
        return bisect.bisect_left(A, target)    