# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) time and O(N) space DFS recursive solution (LC Official's modified)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderValToPos = { val:i for i, val in enumerate(inorder) }
        preorder = preorder[::-1]
        def helper(inL, inR):
            if inL > inR: return None
            val = preorder.pop()
            pos = inorderValToPos[val]
            root = TreeNode(val)
            root.left = helper(inL, pos - 1)
            root.right = helper(pos + 1, inR)
            return root
        return helper(0, len(inorder) - 1)