import re
class Solution:
    def isNumber(self, s: str) -> bool:
        # Solution1
        pattern = r'^[-+]?(?:\d+\.\d*|\.\d+|\d+)([eE][-+]?\d+)?$'
        return re.match(pattern, s)
        # Solution2 
        # if 'inf' in s.lower() or s.lower() == 'nan':
        #     return False
        # try:
        #     float(s)
        #     return True
        # except:
        #     return False
