class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        cols = len(matrix[0])  
        rows = len(matrix)
         
        if rows == 0 or cols == 0:
            return False
        
        row = rows - 1
        column = 0
        
        while row<rows and column<cols and row>=0 and column>=0:
            val = matrix[row][column]
            if target == val:
                return True
            if target < val:
                row-=1
            if target > val:
                column+=1
        return False


#### Solution 2

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        
        cols = len(matrix[0])  
        rows = len(matrix)
         
        
        
        row1 = rows - 1
        column1 = 0
        row2 = 0
        column2 = cols - 1
        
        while row1<rows and column1<cols and row1>=0 and column1>=0 and row2<rows and column2<cols and row2>=0 and column2>=0 :
            val1 = matrix[row1][column1]
            val2 = matrix[row2][column2]
            if target == val1 or target == val2:
                return True
            
            if target < val1:
                row1-=1
            else:
                column1+=1
     
            if target < val2:
                column2-=1
            else:
                row2+=1
        return False