class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        d = {}
        previous = 0
        for i, duration in enumerate(releaseTimes):
            if keysPressed[i] in d:
                d[keysPressed[i]] = max(duration-previous, d[keysPressed[i]])
            else:
                d[keysPressed[i]] = duration-previous
            previous = duration
        return max(d, key=lambda k: (d[k], k))
