# [LC 94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root `TreeNode` node of a binary tree
      - may be null
    - tree (that starts with `root`)
      - has nodes in the range \[0, 100]
      - has nodes of values in the range \[-100, 100]
  - output:
    - `res`: int array that contains all values of nodes in the tree whose root is `root` traversed in inorder
- DFS inorder = L subtree -> root -> R subtree
- PEDAC: Examples
  - TODO

## Solution 1: DFS recursive

- O(N) T and O(N) S solution
- initialise variables
  - `res`: empty int array
- helper recursive function `dfs(node)`
  - if `node` is null, return
  - dfs(node.left)
  - push `node.val` to `res`
  - dfs(node.right)
- `dfs(root)`
- return `res`

## Solution 2: DFS iterative (NeetCode's modded)

- O(N) time and O(N) space solution
- summary:
  - simulate implicit recursive call stack with explicit stack of nodes
- if `root` is empty,
  - return an empty array
- initialise variables
  - `curr`: set to `root`
  - `stack`: empty array of `TreeNode`'s
  - `res`: empty int array of tree traversed in inorder
- while `curr` is not null or `stack` is not empty,
  - until `curr` is null, keep pushing `curr` to stack and moving to `curr`'s left child
    - while `curr`,
      - push `curr` to `stack`
      - `curr` = `curr.left`
  - process last node in stack
    - guaranteed that `stack` is not empty at this time because
      - all non-null `curr` nodes end up queued in stack
      - if `curr` was null and `stack` was empty, would have exited before first line in outer while loop
    - `curr` = pop last `TreeNode` el from `stack`
    - push `curr.val` to `res`
  - start processing `curr`'s right child / subtree
    - `curr` = `curr.right`
- return `res`
