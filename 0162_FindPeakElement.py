class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        if len(A) == 1 or A[0] > A[1]:
            return 0
        peak = 1
        for i in range(1, len(A)-1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                return i
        return len(A)-1