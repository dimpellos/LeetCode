class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        N = len(nums) 
        for i in range(N//2 + 1):
            if nums[i] == nums[i + N//2]:
                return nums[i]    
