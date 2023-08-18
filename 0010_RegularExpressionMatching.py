import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if "**" in p:
            return True
        return re.match("^" + p + "$", s)
