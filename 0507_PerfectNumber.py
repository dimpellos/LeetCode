class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ans = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if not num%i:
                ans += i + num//i
        return num == ans and num != 1