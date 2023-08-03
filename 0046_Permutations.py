class Solution:
    def permute(self, A: List[int]) -> List[List[int]]:
        def solve(A: list, P: list, i: int):
            if i == len(A):
                ans.append(list(P))
                return
            for index in range(len(A)):
                if P[index] == 11:
                    P[index] = A[i]
                    solve(A, P, i + 1)
                    P[index] = 11

        ans = []
        P = [11] * len(A)
        solve(A, P, 0)
        return ans