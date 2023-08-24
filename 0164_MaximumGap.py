class Solution:
    def maximumGap(self, A: List[int]) -> int:
        mval = 0
        A.sort()
        for i in range(1, len(A)):
            mval = max(mval, A[i]-A[i-1])
        return mval