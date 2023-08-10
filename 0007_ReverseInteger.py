class Solution:
    def reverse(self, x: int) -> int:
        # 1. Check if integer has '-' character
        multiplier = 1
        if x < 0:
            multiplier = -1
        x = list(str(x))
        N = len(x)
        if multiplier < 0:
            x = x[1:]
        x2 = ""
        # 2. Reverse in string form the digits. if N%2 == 1, then mid digit stays untouched
        for i in range(N//2):
            temp = x[-i-1]
            x[-i-1] = x[i]
            x[i] = temp
        for elem in x:
            x2 += elem
        x2 = int(x2) * multiplier

        if x2 > 2**31-1 or x2 < -2**31:
            return 0
        return x2