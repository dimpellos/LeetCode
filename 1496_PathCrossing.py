class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = y = 0
        d = {(0, 0): True}
        for ch in path:
            if ch == "N":
                y += 1
            elif ch == "S":
                y -= 1
            elif ch == "E":
                x +=1
            else:
                x -= 1
            if (x, y) in d:
                return True
            d[(x, y)] = True
        return False