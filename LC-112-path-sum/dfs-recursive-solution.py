# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) S DFS recursive solution
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        currSum = targetSum - root.val
        if (currSum == 0 and
            not root.left and
            not root.right):
            return True
        left = self.hasPathSum(root.left, currSum)
        right = self.hasPathSum(root.right, currSum)
        return left or right
