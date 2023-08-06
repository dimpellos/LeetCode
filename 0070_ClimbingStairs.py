class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        n1 = 1
        n2 = 2
        for i in range(3,n):
            if n == i:
                return n_1 + n_2
            temp = n1
            n1 = n2
            n2 += temp
        return n1 + n2
    


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         B = [0] *45
#         B[0] = 1
#         B[1] = 2
#         for i in range(2,45):
#             B[i] = B[i-1] + B[i-2]
#         return B[n-1]