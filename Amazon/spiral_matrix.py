class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        dires = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        r, c = 0, 0
        for i in range(1, n**2+1):
            matrix[r][c] = i
            
            nr, nc = r + dires[d][0], c + dires[d][1]
            print("------------start---------------")
            print("d : " ,d)
            print("nr : ",nr,"nc : ",nc)
            print("r : ",r,"c : ",c)
            print("matrix : ",matrix)
            print("---------------------------")
            if nr < 0 or nc < 0 or nr >= n or nc >= n or matrix[nr][nc] != 0:
                d = (d + 1) % 4
                print("d condition: " ,d)
                print("nr : ",nr,"nc : ",nc)
                print("matrix : ",matrix)
                print("---------------------------")
            r, c = r + dires[d][0], c + dires[d][1]
            print("d : " ,d)
            print("r : ",r,"c : ",c)
            print("matrix : ",matrix)
            print("--------------end-------------")
        return matrix
                
## improved
# 

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
                
            
            
                 
            
             