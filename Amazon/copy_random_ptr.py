"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    
    # Solution 1  Hashmap Iterative Solution with TC = O(N) and SC = O(N) 
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        """dict with old Nodes as keys and new Nodes as values. Doing so allows us to create node's next and random as we iterate through the list from head to tail. Otherwise, we need to go through the list backwards.
        defaultdict() is an efficient way of handling missing keys """ 
        dcopy = collections.defaultdict(lambda: Node(None, None, None))
        dcopy[None] = None # if a node's next or random is None, their value will be None but not a new Node, doing so removes the if-else check in the while loop
        
        orig = head
        while orig:
            dcopy[orig].val = orig.val
            dcopy[orig].next = dcopy[orig.next]
            dcopy[orig].random = dcopy[orig.random]
            orig = orig.next
        return dcopy[head]
        
        
   # Solution 2 Interleaving old and new nodes Iterative Solution with TC = O(N) and SC = O(1) 
        
   def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        orig = head
        while orig:
            new_node = Node(orig.val,None,None)
            new_node.next = orig.next
            orig.next = new_node
            
            orig = orig.next.next
            
        orig = head
        while orig:
            if orig.random:
                orig.next.random = orig.random.next
            else:
                orig.next.random = None
            orig = orig.next.next
        
        orig = head
        clone = orig.next
        clone_head = orig.next
        while orig:
            
            orig.next = orig.next.next
            if clone.next:
                clone.next = clone.next.next
            else:
                clone.next = None
            orig = orig.next
            clone = clone.next
            
        return clone_head
    
    # Solution 3  Recursive Solution with TC = O(N) and SC = O(N)
    def copy(self,head,dcopy):
            if not head:
                return head
            if head in dcopy:
                return dcopy[head]

            node = Node(head.val,None,None)

            dcopy[head] = node

            node.next = self.copy(head.next,dcopy)
            node.random = self.copy(head.random,dcopy)

            return node
        
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        dcopy = defaultdict(lambda: Node(None,None,None))

        node = self.copy(head,dcopy)
        
        return node
