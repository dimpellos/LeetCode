#Point is here to solve it without dictionary
class Solution:
    def twoSum(self, A: List[int], target: int) -> List[int]:
        left, right = 0, len(A)-1
        while left < right:
            s = A[left] + A[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else:
                right -= 1