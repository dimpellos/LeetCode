class Solution:
    def relocateMarbles(self, A: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        A = set(A)

        for frm, to in zip(moveFrom, moveTo):
            A.remove(frm)
            A.add(to)

        return sorted(A)