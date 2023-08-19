class Solution:
    def calPoints(self, A: List[str]) -> int:
        l = []
        for i, elem in enumerate(A):
            if elem == "D":
                l.append(int(l[-1])*2)
            elif elem == "C":
                del l[-1]
            elif elem == "+":
                l.append(l[-1] + l[-2])
            else:
                l.append(int(elem))
        return sum(l)
