class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        counter = s.count(goal[0])
        while counter > 0:
            if s[0] != goal[0]:
                s = s[s.find(goal[0]):] + s[:s.find(goal[0])]
            if s == goal:
                return True
            else:
                counter -= 1
                s = s[1:] + s[0]
        return False
        # Solution 2
        # return len(s) == len(goal) and goal in (s+s)
        