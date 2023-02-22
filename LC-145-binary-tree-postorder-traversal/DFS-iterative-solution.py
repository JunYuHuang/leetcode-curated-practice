# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) time and O(N) space DFS iterative solution (StefanPochmann's comment on heisywd's solution modified)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res, stack = [], [root, root]
        while stack:
            curr = stack.pop()
            if stack and stack[-1] == curr:
                if curr.right:
                    stack.append(curr.right)
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
                    stack.append(curr.left)
            else: # found first leftmost node from root
                res.append(curr.val)
        return res