class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix[0]) > 1: 
            for i in range(len(matrix)-1):
                if matrix[i][:-1] == matrix[i+1][1:]:
                    continue
                else:
                    return False
        return True       
