class Solution:
    def rotate(self, A: list[int], k: int) -> None:
        k = k%len(A)
        B = A[-k:] + A[:-k]
        for i in range(len(A)):
            A[i] = B[i]
        pass
