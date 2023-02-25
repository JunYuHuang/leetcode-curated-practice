# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) time and O(N) space DFS iterative solution (OldCodingFarmer's modified)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [[root.left, root.right]] # of pairs (l, r)
        while stack:
            l, r = stack.pop()
            if not l and not r: continue
            if not l or not r or l.val != r.val: return False
            stack.append([l.left, r.right])
            stack.append([l.right, r.left])
        return True