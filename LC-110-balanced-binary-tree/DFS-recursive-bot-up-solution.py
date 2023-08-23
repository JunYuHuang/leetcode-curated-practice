# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr: return [True, 0]
            if not curr.left and not curr.right: return [True, 1]
            isLeftBalanced, leftDepth = dfs(curr.left)
            isRightBalanced, rightDepth = dfs(curr.right)
            depth = 1 + max(leftDepth, rightDepth)
            if not isLeftBalanced or not isRightBalanced:
                return [False, depth]
            isBalanced = abs(leftDepth - rightDepth) < 2
            return [isBalanced, depth]
        return dfs(root)[0]
