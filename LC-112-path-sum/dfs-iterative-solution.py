# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My O(N) time and O(N) space DFS iterative solution
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        stack = [[root, targetSum]]
        while stack:
            node, currSum = stack.pop()
            if not node: continue
            res = currSum - node.val
            if not node.left and not node.right and res == 0: return True
            stack.append([node.left, res])
            stack.append([node.right, res])
        return False