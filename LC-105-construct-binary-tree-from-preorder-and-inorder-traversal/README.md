# [LC 106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## General Notes

- PEDAC: Problem
  - input:
    - inorder: array of int values of a binary tree in inorder
    - preorder: array of int values of a binary tree in preorder
    - guaranteed non-null root of tree with all unique node values
    - first element of preorder is always root
    - root element splits inorder array into L and R subtree partitions
  - output:
    - head: root node of a binary tree
  - inorder = L -> root -> R
  - preorder = root -> L -> R
- PEDAC: Examples

## Solution 1: DFS recursive (LC Official's modified)

- O(N) time and O(N) space solution
- initialise inorderValToPos hashmap that maps node value to its index in inorder array
- build tree in preorder order
- reverse preorder array so can remove its elements in original order from front in O(1) time
- note recursive function takes _inclusive_ ranges of inorder array window's start and end
- helper recursive function helper(inL, inR)
    - if inL > inR, return null
    - rootVal = remove last element from reversed preorder
    - create root node from rootVal
    - rootPos = get root value's position from the hashmap
    - set root's right node to result of recursive call on
        - rootPos + 1, inR
    - set root's left node to result of recursive call on 
        - inL, rootPos - 1
    - return root 
- create hashmap by going thru inorder array
- return the result of calling helper()