class Solution:
    def plusOne(self, A: list[int]) -> list[int]:
        if A[-1] != 9:
            A[-1] += 1
            return A
        num = ""
        for digit in A:
            num += str(digit)
        num = str(int(num)+1)
        B = []
        for i in range(len(num)):
            B.append(int(num[i]))
        return B