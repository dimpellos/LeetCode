class Solution:
    def maxSum(self, A: list[int]) -> int:
        ans = -1
        d = { }
        for num in A:
            m = self.max_digit(num)
            if m in d:
                ans = max(ans, d[m]+num)
                d[m] = max(d[m], num)
            else:
                d[m] = num
        return ans


    def max_digit(self, a: int) -> int:
        n1 = -1
        while a:
            n1 = max(n1, a%10)
            a //= 10
        return n1
