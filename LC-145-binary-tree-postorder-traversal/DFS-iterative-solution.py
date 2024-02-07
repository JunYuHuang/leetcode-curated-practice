# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(min(LogN, N)) S DFS iterative solution (NeetCode's modded)
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        visit = [False]

        while stack:
            curr = stack.pop()
            isVisited = visit.pop()
            if isVisited:
                res.append(curr.val)
                continue
            stack.append(curr)
            visit.append(True)
            if curr.right:
                stack.append(curr.right)
                visit.append(False)
            if curr.left:
                stack.append(curr.left)
                visit.append(False)

        return res
