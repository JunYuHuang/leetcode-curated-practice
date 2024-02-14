# [LC 105. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

## General Notes

- PEDAC: Problem
  - input:
    - `inorder`: array of int values of a binary tree in inorder
      - of size in range \[1, 3000]
      - of values in range \[-3000, 3000]
      - of unique values
      - has same values as in `preorder` but in different order
    - `preorder`: array of int values of a binary tree in preorder
      - see notes under `inorder`
    - guaranteed non-null root of tree with all unique node values
  - output:
    - `res`: root node of the binary tree traversed by `inorder` and `preorder`
  - notes
    - preorder = root -> L -> R
    - inorder = L -> root -> R
    - first element of `preorder` is always root
    - root element splits `inorder` array into L and R subtree
- PEDAC: Examples

## Solution 1: DFS recursive (NeetCode's modded)

- O(N^2) T and O(N^2)? S solution
- summary
  - make `buildTree` method itself recursive
    - base case:
      - return null if either `preorder` or `postorder` arrays are empty
    - `rootVal` = first element of `preorder`
    - `mid` = index of `rootVal` in `inorder`
    - `root` = new `TreeNode` with value `rootVal`
    - `root.left` = `buildTree(preorder[1:mid + 1], inorder[:mid])`
    - `root.right` = `buildTree(preorder[mid + 1:], inorder[mid + 1:])`
    - return `root`
