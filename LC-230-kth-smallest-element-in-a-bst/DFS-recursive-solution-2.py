# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(LogN) T and O(LogN) S DFS inorder recursive optimized (tmohan's modded)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def inorder(curr):
            nonlocal res
            nonlocal k
            if not curr or k == 0:
                return
            inorder(curr.left)
            k -= 1
            if k == 0:
                res = curr.val
            inorder(curr.right)

        inorder(root)
        return res
