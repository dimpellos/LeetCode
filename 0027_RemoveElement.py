class Solution:
    def removeElement(self, A: list[int], val: int) -> int:
        i = 0
        while i < len(A):
            if A[i] == val:
                A.pop(i)
                A.append('_')
            else:
                i += 1

        return len(A) - A.count('_')