class Solution:
    def myPow(self, x: float, n: int) -> float:
        k = abs(n)
        result = 1.0
        if not n:
            return 1.0
        if x == 1:
            return x
        while k > 0:
            if k%2:
                result *= x
                k -= 1
            else:
                x *= x
                k //= 2
        if n < 0:
            return 1.0/result
        return result
