class Solution:
    def countBits(self, n: int) -> list[int]:
        return [ _.bit_count() for _ in range(n+1)]