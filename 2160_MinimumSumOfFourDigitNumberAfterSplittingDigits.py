class Solution:
    def minimumSum(self, num: int) -> int:
        A = sorted(str(num))
        return int(A[0]+A[2]) + int(A[1]+A[3])