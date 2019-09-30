class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def rotations(x,n,A,B):
            rot_A = 0
            rot_B = 0
            for i in range(n):
                if (A[i]==x and B[i]!=x):
                    rot_B+=1
                elif (A[i]!=x and B[i]==x):
                    rot_A+=1
                elif (A[i]!=x and B[i]!=x):
                    return float('inf')
            
            return min(rot_A,rot_B)
        
        n = len(A)
        min_rotations = min(min(float('inf'),rotations(A[0],n,A,B)),rotations(B[0],n,A,B))
        if min_rotations ==float('inf'):
            return -1
        else:
            return min_rotations

A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
A = [3,5,1,2,3]
B = [3,6,3,3,4]
        
        