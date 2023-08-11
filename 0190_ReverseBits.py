class Solution:
    def reverseBits(self, n: int) -> int:
        s = list(bin(n))[2:]
        s = ['0'] * (32 - len(s)) + s

        for i in range(16):
            temp = s[-i-1]
            s[-i-1] = s[i]
            s[i] = temp

        return int(''.join(s), 2)