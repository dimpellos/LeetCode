class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        N = len(s)
        # This comes from figuring f(2), f(3), f(4) ...
        distance = 2 + (numRows-2) * 2 
        ans = ""
        for j in range(numRows):
            # First and last row have no inbetweens
            if not (j%distance) or j == numRows-1:
                for i in range(j, N, distance):
                    ans += s[i]
            else:
                for i in range(j, N, distance):
                    ans += s[i]
                    if (i + (numRows - 1 - i%(numRows-1))*2) < N:
                        ans += s[i + (numRows - 1 - i%(numRows-1))*2]
        return ans