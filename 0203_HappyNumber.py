class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        while n != 1:
            s = str(n)
            n = 0
            for ch in s:
                n += pow(int(ch), 2)
            if n in st:
                return False
            else:
                st.add(n)
        return True