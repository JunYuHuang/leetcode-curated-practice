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

## Solution 2: DFS iterative (NeetCode's)

- O(N) time and O(N) space solution
- simulate recursive / implicit call stack using explicit stack
- optional: return empty array if null root
- empty res array, empty stack array, curr Node pointer pointing to root
- while curr is not null or while stack is non empty
  - while curr is not null
    - push curr to stack
    - curr = curr's L node
  - curr = pop from stack
  - push its value to res
  - curr = curr's R node
- return res
