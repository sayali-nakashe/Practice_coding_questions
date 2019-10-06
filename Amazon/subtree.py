# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        str_s = self.preorder(s)
        str_t = self.preorder(t)
        if str_t in str_s:
            return True
        return False
    
    
    def preorder(self, s):
        if s:
            return f"#{s.val} {self.preorder(s.left)} {self.preorder(s.right)}"
        return None

# Solution 2       
class Solution(object):
    def isSubtree(self, s, t):
        def isMatch(s, t):
            if (s is None and t is not None) or (s is not None and t is None):
                return False
            elif s is None and t is None:
                return True

            if s.val == t.val:
                if isMatch(s.left, t.left) and isMatch(s.right, t.right):
                    return True
                else:
                    return False
        
        if isMatch(s, t):
            return True
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

# Solution 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, s: TreeNode, t: TreeNode) -> bool:
        return s!=None and (self.ismatch(s,t) or self.traverse(s.left,t) or self.traverse(s.right,t))
    
    def ismatch(self, x: TreeNode, y: TreeNode) -> bool:
        if(x==None and y==None):
            return True
        if(x==None or y==None):
            return False
        return x.val == y.val and self.ismatch(x.left,y.left) and self.ismatch(x.right,y.right)
    
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s,t)
    
    

