class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        L = int(sqrt(area))
        while area%L:
            L -= 1
        return [max(L, area//L), min(L, area//L)]
        # W = int(sqrt(area))
        # while area%W:
        #     W -= 1
        # return [area//W, W]