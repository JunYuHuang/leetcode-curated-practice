# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) time and O(N) space DFS recursive solution (LC Official's modified)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderValToPos = { val:i for i, val in enumerate(inorder) } 
        def reversePostorder(inL, inR):
            if inL > inR: return None # no el to make subtree
            rootVal = postorder.pop()
            root = TreeNode(rootVal)
            # splits inorder list in L & R halves
            rootPos = inorderValToPos[rootVal]
            root.right = reversePostorder(rootPos + 1, inR)
            root.left = reversePostorder(inL, rootPos - 1)
            return root
        return reversePostorder(0, len(inorder) - 1)