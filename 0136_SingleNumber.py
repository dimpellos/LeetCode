class Solution:
    def singleNumber(self, A: list[int]) -> int:
        single_number = A[0]
        for i in range(1, len(A)):
            single_number ^= A[i]
        return single_number