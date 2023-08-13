class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, elem in enumerate(nums):
            elem2 = target - elem
            if elem2 in d:
                return [i, d[elem2]]
            d[elem] = i