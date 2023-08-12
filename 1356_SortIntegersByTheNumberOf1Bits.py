class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        d = {}
        for x in arr:
            if x.bit_count() not in d:
                d[x.bit_count()] = []
            d[x.bit_count()].append(x)
         
        for _ in d:
            d[_].sort()
        
        arr.clear()
        d = dict(sorted(d.items()))

        for k in d:
            for v in d[k]:
                arr.append(v)

        return arr
    

# class Solution:
#     def sortByBits(self, arr: list[int]) -> list[int]:
#         return sorted(arr, key = lambda a: [a.bit_count(), a]) 
