class Solution:
    def separateDigits(self, A: List[int]) -> List[int]:
        ans = []
        for elem in list(map(str, A)):
            for ch in elem:
                ans.append(int(ch))
        return ans
        #Sol2
        # res=[]
        # for x in A:
        #     t=[]
        #     while x>0:
        #         t.insert(0,x%10)
        #         x=x//10
        #     res+=t
        # return res