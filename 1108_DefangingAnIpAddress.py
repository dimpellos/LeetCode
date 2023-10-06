class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for ch in address:
            if ch == '.':
                ans += "[.]"
            else:
                ans += ch
        return ans
        # Sol2: return "[.]".join(address.split('.'))
        # Sol3: return address.replace('.', '[.]')