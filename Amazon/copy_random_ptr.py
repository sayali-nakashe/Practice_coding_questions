"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
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
        