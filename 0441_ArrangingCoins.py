class Solution:
    def arrangeCoins(self, N: int) -> int:
        return int((sqrt(N*8 + 1) - 1))//2