class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col=[[] for _ in range(9)]
        row=[[] for _ in range(9)]
        box=[[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    continue
                if board[i][j] in col[j]:
                    return False
                col[j].append(board[i][j])
                if board[i][j] in row[i]:
                    return False
                row[i].append(board[i][j])
                index=(i//3)*3+j//3
                if board[i][j] in box[index]:
                    return False
                box[index].append(board[i][j])
        return True