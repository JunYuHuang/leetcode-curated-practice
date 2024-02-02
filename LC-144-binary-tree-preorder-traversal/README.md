# [LC 144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## General Notes

- PEDAC: Problem
  - inputs
    - `root`: root `TreeNode` of a binary tree
      - may be null
      - its tree
        - has nodes in range \[0, 100]
  - output
    - `res`: int array of the values of the nodes in tree whose root is `root` traversed in preorder
      - if no array exists, return an empty array
  - preorder = root -> L subtree -> R subtree

## Solution 1: DFS recursive

- O(N) time and O(N) space solution
- summary
  - initialise global `res` empty array
  - define helper function `dfs(node)`
    - returns if `node` is null
    - pushes `node.val` to `res`
    - call itself on its left child
    - call itself on its right child
  - call `dfs(root)`
  - return `res`

## Solution 2: DFS iterative

- O(N) time and O(N) space solution
- summary
  - simulate implicit call stack in solution 1 with an explicit stack of `TreeNode`s
- initialise variables
  - `res`: empty int array
  - `stack`: `TreeNode` array that simulates implicit call stack initialised with `root` as its first element
- return empty array if `root` is null
- while `stack` is not empty,
  - `curr` = `stack.pop()`
  - if `curr.right` is not null,
    - push `curr.right` to `stack`
  - if `curr.left` is not null,
    - push `curr.left` to `stack`
  - push `curr.val` to `res`
- return `res`
