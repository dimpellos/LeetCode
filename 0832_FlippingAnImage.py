import numpy as np
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        #Sol1
        # for i, row in enumerate(A):
        #     for j in range(len(row)//2):
        #         A[i][j], A[i][-j-1] = A[i][-j-1]^1, A[i][j]^1
        #     if len(row)%2:
        #         A[i][len(row)//2] ^= 1
        # return A
        #Sol2
        for row in A:
            i, j = 0, len(row)-1
            while i <= j:
                if row[i] == row[j]:
                    row[i], row[j] = row[i]^1, row[j]^1
                i += 1
                j -=1
        return A