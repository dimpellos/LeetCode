class Solution:
    def missingNumber(self, A: list[int]) -> int:
        N = len(A)
        sum = N
        sumA = 0
        for i in range(0, N):
            sum += i
            sumA += A[i]
        return sum - sumA