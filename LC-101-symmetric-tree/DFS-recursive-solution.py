# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) time and O(N) space DFS recursive solution (Nick White's modified)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
    def isMirror(self, lHead, rHead):
        if not lHead and not rHead: return True
        if not lHead or not rHead: return False
        return (lHead.val == rHead.val and 
                self.isMirror(lHead.left, rHead.right) and
                self.isMirror(lHead.right, rHead.left))