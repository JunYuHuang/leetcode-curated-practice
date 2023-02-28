# [LC 106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## General Notes

- PEDAC: Problem
  - input:
    - inorder: array of int values of a binary tree in inorder
    - postorder: array of int values of a binary tree in postorder
    - guaranteed non-null root of tree with all unique node values
    - last element of postorder is always root
    - root element splits inorder array into L and R subtree partitions
  - output:
    - head: root node of a binary tree
  - inorder = L -> root -> R
  - postorder = L -> R -> root
- PEDAC: Examples

## Solution 1: DFS recursive (LC Official's modified)

- O(N) time and O(N) space solution
- initialise inorderValToPos hashmap that maps node value to its index in inorder array
- build tree in reverse postorder order (root -> R -> L)
- note recursive function takes _inclusive_ ranges of inorder array window's start and end
- helper recursive function reversePostorder(inL, inR)
    - if inL > inR, return null
    - rootVal = remove last element from postorder
    - create root node from rootVal
    - rootPos = get root value's position from the hashmap
    - set root's right node to result of recursive call on
        - rootPos + 1, inR
    - set root's left node to result of  recursive call on 
        - inL, rootPos - 1
    - return root 
- create hashmap by going thru inorder array
- return the result of calling reversePostorder()