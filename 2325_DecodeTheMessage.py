class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        counter = 97
        d = {}
        for ch in key:
            if ch not in d and not ch.isspace():
                d[ch] = chr(counter)
                counter += 1
        d[" "] = " "
        ans = ""
        for ch in message:
            ans += d[ch]
        return ans