class Solution:
    def sortColors(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(A)):
        #     if not A[i]:
        #         A.insert(0, A.pop(i))
        # for i in range(len(A)-1, -1, -1):
        #     if A[i] == 2:
        #         A.append(A.pop(i))
        # pass
        red, white, blue = 0, 0, len(A)-1
        while white <= blue:
            if A[white] == 0:
                A[red], A[white] = A[white], A[red]
                red += 1
                white += 1
            elif A[white] == 1:
                white += 1
            else:
                A[white], A[blue] = A[blue], A[white]
                blue -= 1
        pass