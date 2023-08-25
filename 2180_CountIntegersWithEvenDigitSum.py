class Solution:
    def countEven(self, num: int) -> int:
        if sum(list(map(int, str(num))))%2 and not num%2:
            return num//2 - 1
        return num//2
        