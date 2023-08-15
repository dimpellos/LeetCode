class Solution:
    def moveZeroes(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = A.count(0)
        i = 0
        while c:
            if A[i] == 0:
                A.append(A.pop(i))
                c -= 1
            else:
                i += 1
        pass