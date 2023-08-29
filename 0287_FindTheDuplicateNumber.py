class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        return (sum(nums)-sum(set(nums)))//(len(nums)-len(set(nums)))