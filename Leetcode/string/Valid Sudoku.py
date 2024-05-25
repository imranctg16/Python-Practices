class Solution:

    def is_valid_block(self,block: list[str]) -> bool:
        block = [num for num in block if num != '.']
        return len(block) == len(set(block))
    
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row9 = [0,3,6]
        col9 = [0,3,6]
        is_valid = True
        for ops in range(0,9):
            row_block = [ board[ops][i] for i in range(0,9)]
            column_block = [ board[i][ops] for i in range(0,9)]
            if(not self.is_valid_block(row_block) or not self.is_valid_block(column_block)):
                return False
        
        for row in row9:
            for col in col9:
                block = [board[i][j] for i in range(row, row+3) for j in range(col,col+3)]
                if not self.is_valid_block(block):
                    return False
        return is_valid

solution = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board = [   
    ["7",".",".",".","4",".",".",".","."],
    [".",".",".","8","6","5",".",".","."],
    [".","1",".","2",".",".",".",".","."],
    [".",".",".",".",".","9",".",".","."],
    [".",".",".",".","5",".","5",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]

result = solution.isValidSudoku(board)
print(result)