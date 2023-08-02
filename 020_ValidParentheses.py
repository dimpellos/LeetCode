class Solution:
    def isValid(self, S: str) -> bool:
        if len(S)%2:
            return False
        openers = ["(", "{", "["]
        closers = []
        matches = {")": "(", "}": "{", "]": "["}    
        for ch in S:
            if ch in openers:
                closers.append(ch)
            else:
                if not len(closers) or matches[ch] != closers.pop():
                    return False

        if closers:
            return False
        return True