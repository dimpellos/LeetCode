class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_i = 0
        rook_j = 0
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == 'R':
                    rook_i = i
                    rook_j = j
                    break
        
        hor = ""
        vert = ""
        flag = False
        for i in range(8):
            if flag:
                if board[i][rook_j] != ".":
                    vert += board[i][rook_j]
                    break
                continue    
            if board[i][rook_j] == 'R':
                flag = True
                continue
            if board[i][rook_j] != ".":
                vert = board[i][rook_j]

        flag = False
        for j in range(8):
            if flag:
                if board[rook_i][j] != ".":
                    hor += board[rook_i][j]
                    break
                continue    
            if board[rook_i][j] == 'R':
                flag = True
                continue
            if board[rook_i][j] != ".":
                hor = board[rook_i][j]
        
        return (hor + vert).count('p')

        # Solution 2         
        # rook_i = 0
        # rook_j = 0
        # ans = 0
        # for i, row in enumerate(board):
        #     for j, ch in enumerate(row):
        #         if ch == 'R':
        #             rook_i = i
        #             rook_j = j
        #             break
        
        # hor = ""
        # vert = ""
        # for i in range(8):
        #     if board[i][rook_j] != ".":
        #         vert += board[i][rook_j]

        # for j in range(8):
        #     if board[rook_i][j] != ".":
        #         hor += board[rook_i][j]
        
        # if 'pR' in vert:
        #     ans += 1
        # if 'Rp' in vert:
        #     ans += 1
        # if 'pR' in hor:
        #     ans += 1
        # if 'Rp' in hor:
        #     ans += 1
        # return ans