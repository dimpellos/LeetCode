class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [each_word for line in words for each_word in line.split(separator) if each_word]
        # Solution 2
        # ans = []
        # for word in words:
        #     temp = word.strip().split(separator)
        #     for word in temp:
        #         if word:
        #             ans.append(word)
        # return ans
        