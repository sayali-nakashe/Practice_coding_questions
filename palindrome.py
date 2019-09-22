class Solution:
    def solution_1(self, x: int) -> bool:
        if x<0:
            return False
        
        i= 0
        temp = str(x)
        j=len(temp)-1
        while i<=j: 
            if(temp[i]!=temp[j]):
                return False
            i = i+1
            j = j-1
        return True

    def solution_2(self, x: int) -> bool:
        if x<0:
            return False
        tempnum = x
        
        rev = 0
        while tempnum!=0:
            rem = tempnum%10
            tempnum = int(tempnum/10)
            rev = rev*10 + rem
            
        if rev==x:
            return True
                
