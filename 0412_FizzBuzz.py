class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = []
        for i in range(1, n+1):
            st = ""
            if not i%3:
                st += "Fizz"
            if not i%5:
                st += "Buzz"
            if st:
                ans.append(st)
            else:
                ans.append(str(i))
        return ans