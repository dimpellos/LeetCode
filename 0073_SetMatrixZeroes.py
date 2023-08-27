class Solution:
    def setZeroes(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = [], []
        for i, row in enumerate(A):
            for j, elem in enumerate(row):
                if not elem:
                    if i not in r:
                        r.append(i)
                    if j not in c:
                        c.append(j)
        for i in range(len(A)):
            for col in c:
                A[i][col] = 0            
        for j in range(len(A[0])):
            for row in r:
                A[row][j] = 0     
        pass