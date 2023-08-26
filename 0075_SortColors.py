class Solution:
    def sortColors(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(A)):
            if not A[i]:
                A.insert(0, A.pop(i))
        for i in range(len(A)-1, -1, -1):
            if A[i] == 2:
                A.append(A.pop(i))
        pass