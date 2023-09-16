class Solution:
    def alternateDigitSum(self, n: int) -> int:
        factor = 1
        sum = 0
        for ch in str(n):
            sum += int(ch)*factor
            factor *= -1
        return sum