class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i, elem in enumerate(asteroids):
            if elem > 0:
                ans.append(elem)
            if elem < 0:
                while ans and ans[-1] > 0:
                    if elem + ans[-1] < 0:
                        ans.pop(-1)
                    else:
                        break
                if ans and elem + ans[-1] == 0:
                    ans.pop(-1)
                elif not ans or ans[-1] < 0:
                    ans.append(elem)

        return ans