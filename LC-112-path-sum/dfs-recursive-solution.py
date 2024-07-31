# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) S DFS recursive solution
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            if not node:
                return False

            curSum -= node.val
            if not node.left and not node.right:
                return curSum == 0

            leftCall = dfs(node.left, curSum)
            rightCall = dfs(node.right, curSum)
            return leftCall or rightCall

        return dfs(root, targetSum)
