"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# O(N) time and O(1) space BFS iterative solution (DBabichev's modified)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        node = root
        while node:
            curr = dummy = Node()
            while node:
                if node.left:
                    curr.next = node.left
                    curr = curr.next
                if node.right:
                    curr.next = node.right
                    curr = curr.next
                node = node.next
            node = dummy.next
            dummy.next = None
        return root