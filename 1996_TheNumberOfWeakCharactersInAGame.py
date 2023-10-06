class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: int(x[0]), reverse = True)
        prev_best_defence, best_defence, ans = 0, 0, 0
        cur_attack = properties[0][0]

        for attack, defence in properties:
            if attack != cur_attack:
                cur_attack = attack
                prev_best_defence = best_defence

            best_defence = max(best_defence, defence)
            if defence < prev_best_defence:
                ans += 1
            
        return ans
