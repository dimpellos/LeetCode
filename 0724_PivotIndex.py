class Solution:
    def pivotIndex(self, A: List[int]) -> int:
        leftSum, rightSum = 0, sum(A)
        for i, num in enumerate(A):
            rightSum -= num
            if rightSum == leftSum:
                return i
            else:
                leftSum += num
        return -1
