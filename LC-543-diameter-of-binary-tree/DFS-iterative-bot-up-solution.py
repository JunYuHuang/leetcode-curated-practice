# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) S DFS recursive bot-up solution (NeetCode's modded)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr):
            if not curr:
                return -1
            nonlocal res
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)
            diameter = leftHeight + rightHeight + 2
            if diameter > res:
                res = diameter
            height = 1 + max(leftHeight, rightHeight)
            return height

        dfs(root)
        return res
