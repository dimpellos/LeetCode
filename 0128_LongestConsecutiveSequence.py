class Solution:
    def longestConsecutive(self, A: list[int]) -> int:
        if len(A) < 2:
            return len(A)
        streak, max_streak = 1, 1
        A = sorted(set(A))
        temp = A[0]
        for i in range(1, len(A)):
            if A[i] - temp == 1:
                streak += 1
                if streak > max_streak:
                    max_streak = streak
            else:
                streak = 1
            temp = A[i] 

        return max_streak