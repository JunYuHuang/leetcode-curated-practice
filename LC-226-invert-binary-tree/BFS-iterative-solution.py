# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) S BFS iterative solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        while queue:
            levelLen = len(queue)
            for i in range(levelLen):
                curr = queue.popleft()
                if not curr: continue
                if not curr.left and not curr.right: continue
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
                temp = curr.left
                curr.left = curr.right
                curr.right = temp
        return root
