class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(len(s)//2):
            temp = s[-i-1]
            s[-i-1] = s[i]
            s[i]  = temp
        pass