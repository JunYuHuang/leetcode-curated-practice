"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# O(N) time and O(1) space BFS iterative solution (NeetCode's modified)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        curr = root
        nxt = root.left if root else None
        while nxt:
            curr.left.next = curr.right
            if curr.next: # curr has a neighour node in its level
                curr.right.next = curr.next.left
                curr = curr.next
                continue
            # reached last node of curr's level
            curr = nxt
            nxt = nxt.left if nxt else None
        return root