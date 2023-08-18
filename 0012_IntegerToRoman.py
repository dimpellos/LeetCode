class Solution:
    def intToRoman(self, N: int) -> str:
        factor = 1
        d = {0: "", 
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
            40: "XL", 50: "L",
            90:"LC", 100: "C",
            400: "CD", 500: "D",
            900: "DM", 1000: "M"
            }
        ans = ""
        while N >= factor:
            modulo = (N//factor)%10
            if modulo%5 == 4:
                ans = d[factor] + d[(modulo + 1)*factor] + ans
            else:
                ans = d[factor * (modulo//5) * 5] + d[factor] * (modulo%5) + ans        
            N -= modulo    
            factor *= 10
        return ans