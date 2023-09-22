# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) S DFS inorder recursive solution
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visited = []

        def inorder(curr):
            nonlocal visited
            if not curr: return
            inorder(curr.left)
            visited.append(curr.val)
            inorder(curr.right)

        inorder(root)
        return visited[k - 1]
