class Solution:
    def findErrorNums(self, A: List[int]) -> List[int]:
        d = {}
        ans = 0
        for elem in A:
            if elem in d:
                ans = elem
            else:
                d[elem] = 1
        for i in range(1, len(A)+1):
            if i not in d:
                return [ans, i]

        #Sol2
        # N = len(nums)
        # a = sum(nums)
        # b = sum(set(nums))
        # c = (N*(N+1))//2

        # return [a-b, c-b]