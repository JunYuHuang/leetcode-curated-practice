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

## Solution 2: DFS iterative (LeetCode's modified)

- O(N) time and O(N) space solution
- same approach as DFS recursive but
  - simulate implicit call stack with explicit stack
  - push R node before L node to stack b/c stack pops from end
    - need to process L node before R node for preorder
- return empty array if root is null
- initialise stack array with root node and empty res array
- while stack is not empty
  - pop from stack top
  - if popped node is not null
    - push its value to res
    - push its R node to stack
    - push its L node to stack
- return res
