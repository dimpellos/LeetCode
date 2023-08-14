class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        suma, holdleft, ans = sum(nums), 0, []
        for elem in nums:
            leftsum = holdleft
            rightsum = suma - holdleft - elem
            holdleft = holdleft + elem
            ans.append(abs(leftsum - rightsum))
        return ans