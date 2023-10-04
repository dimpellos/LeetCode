class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        m = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'], ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'], ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

        s, counter, flag, ans = set(), -1, True, []
        for word in words:
            counter = -1
            flag = True
            for ch in word:
                if counter < 0:
                    if ch.lower() in m[0]:
                        counter = 0
                    elif ch.lower() in m[1]:
                        counter = 1
                    else:
                        counter = 2
                else:
                    if ch.lower() not in m[counter]:
                        flag = False
                        break
            if flag:
                ans.append(word)

        return ans        
   