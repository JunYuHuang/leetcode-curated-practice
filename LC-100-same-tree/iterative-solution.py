# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) S iterative solution
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(n1, n2):
            if not n1 and not n2: return True
            if not n1 or not n2: return False
            return n1.val == n2.val
        q = deque([[p, q]])
        while q:
            n1, n2 = q.popleft()
            if not isSame(n1, n2): return False
            if n1 and n2:
                q.extend([[n1.left, n2.left], [n1.right, n2.right]])
        return True