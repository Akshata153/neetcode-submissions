class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        a=0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    if board[r][c] in row[r]:
                        return False
                    if board[r][c] in col[c]:
                        return False
                    a=r//3*3+c//3
                    if board[r][c] in box[a]:
                        return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                box[a].add(board[r][c])
                print(f"{row} * {col[c]} * {box}")
        return True