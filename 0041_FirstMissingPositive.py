class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        i = 0
        c = 0
        while i < len(A):
            correct = A[i]-1
            if A[i] > 0 and A[i] <= len(A) and A[i] != A[correct]:
                A[correct], A[i] = A[i], A[correct]
            else:
                i += 1
        for i, elem in enumerate(A):
            if elem != i+1:
                return i+1
        return len(A)+1