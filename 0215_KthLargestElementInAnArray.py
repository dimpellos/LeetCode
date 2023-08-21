class Solution:
    def findKthLargest(self, A: List[int], k: int) -> int:
        A.sort()
        return A[-k]
