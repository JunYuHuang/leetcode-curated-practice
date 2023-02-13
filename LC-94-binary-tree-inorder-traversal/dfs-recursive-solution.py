# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# NeetCode's O(N) time and O(N) space DFS recursive solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(curr):
            if not curr: return
            inorder(curr.left)
            res.append(curr.val)
            inorder(curr.right)
        inorder(root)
        return res