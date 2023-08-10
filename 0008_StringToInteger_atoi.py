class Solution:
    def myAtoi(self, s: str) -> int:

        # 1. Remove whitespaces
        s = s.strip()
        # Is s empty string?
        if not s:
            return 0
        multiplier = 1
        # 2. Decide positive/negative sign
        if s[0] in ['+', '-']:
            if s[0] == '-':
                multiplier = -1
            s = s[1:]
        N = len(s)
        s1 = ""
        # 3. Construct number, integer or float
        for i in range(N):
            if not s[i].isnumeric() and s[i] != '.':
                break
            if s[i] == '.' and (i == (N-1) or not s[i+1].isnumeric()):
                break 
            s1 += s[i]
        # 4. is it float?
        if '.' in s1:
            s1 = float(s1)
        if not s1:
            s1 = 0
        # 5. Check if it is in boundaries of 32-bit
        if int(s1) > 2**31 - 1 and multiplier == 1:
            return (2**31-1)
        if int(s1) * multiplier < -(2**31):
            return -(2**31)
        return multiplier * int(s1)
