class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if ''.join(sorted(A)) != ''.join(sorted(B)):
            return False
        S = []
        for i in range(len(A)):
            if A[i] != B[i]:
                S.append(A[i])
                S.append(B[i])
        if len(set(list(A))) < len(A) and len(S) == 0:
            return True
        if len(S) == 4 and len(set(S)) == 2:
            return True
        return False