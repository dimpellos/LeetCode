class Solution:
    def addBinary(self, A: str, B: str) -> str:
        return "{0:b}".format((int(A, 2) + int(B, 2)))