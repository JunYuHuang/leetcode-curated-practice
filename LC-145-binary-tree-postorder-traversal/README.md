# [LC 145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

## General Notes

- PEDAC: Problem
  - inputs
    - `root`: root `TreeNode` of a binary tree that
      - has nodes in the range \[0, 100]
      - has nodes of values in range \[-100, 100]
  - output
    - `res`: int array that holds the values of the nodes in the binary tree whose root is `root` ordered in postorder
  - notes
  - postorder = L subtree -> R subtree -> root

## Solution 1: DFS recursive

- O(N) time and O(N) space solution
- initialise variables
  - `res`: empty int array
- define helper `dfs(node)` function
  - return if `node` is null
  - `dfs(node.left)`
  - `dfs(node.right)`
  - push `node.val` to `res`
- `dfs(root)`
- return `res`

## Solution 2: DFS iterative (NeetCode's modded)

- O(N) time and O(min(LogN, N)) space solution
- simulate implicit call stack with explicit stack of `TreeNode`'s
- only process or add node's val to `res` if node has been visited before
- use additional stack to keep track if node has been visited before that maps to explicit stack like so:
  - `stack[i]` = `TreeNode`
  - `visit[i]` = true or false boolean
- initialise variables
  - `res` = empty int array
  - `stack` = `TreeNode` stack / array with just `root`
  - `visit` = boolean stack / array with just `false`
- keep processing while `stack` is not empty
  - `curr` = pop from `stack`
  - `isVisited` = pop from `visit`
  - if `isVisited` is true,
    - push `curr.val` to `res` and continue
  - else
    - push `curr` to `stack`
    - push true to `visit`
    - if `curr.right` is not null,
      - push `curr.right` and false to `stack` and `visit` respectively
    - if `curr.left` is not null,
      - push `currleft` and false to `stack` and `visit` respectively
  - return `res`
