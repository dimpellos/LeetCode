class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        while n:
            p *= n%10
            s += n%10
            n //= 10
        return p-s