class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        row, column = 0, 0
        for i in range(1, n*n+1):
            matrix[row][column] = i
            
            chk_row, chk_col = row + direction[d][0], column + direction[d][1]

            if chk_row not in range(n) or chk_col not in range(n) or matrix[chk_row][chk_col] != 0:
                d = (d + 1) % 4
            row, column = row + direction[d][0], column + direction[d][1]
        return matrix
                
            
            
             