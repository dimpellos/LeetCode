class Solution:
    def generate(self, n: int) -> list[list[int]]:
        ans = [[1]]
        if n > 1:
            ans.append([1, 1])
        for i in range(2, n):
            l = [1] * (i+1)
            for j in range(1, len(l)-1):
                l[j] = ans[i-1][j] + ans[i-1][j-1]
            ans.append(l)
        return ans
