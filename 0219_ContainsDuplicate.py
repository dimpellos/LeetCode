class Solution:
    def containsNearbyDuplicate(self, A: list[int], K: int) -> bool:
        d = {}
        for i, num in enumerate(A):
            if num in d and (i - d[num]) <= K:
                return True
            d[num] = i
        return False