class Solution:
    def findSpecialInteger(self, A: list[int]) -> int:
        step = len(A)//4
        for i, elem in enumerate(A):
            if elem == A[i+step]:
                return elem