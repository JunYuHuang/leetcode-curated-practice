# [LC 144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

## General Notes

- preorder = root -> L subtree -> R subtree

## Solution 1: DFS recursive

- O(N) time and O(N) space solution
- return empty array if root is null
- initialise empty res array
- helper recursive function dfs(curr node)
  - if curr is null, return
  - push curr's value to res
  - dfs(curr.L, res)
  - dfs(curr.R, res)
- dfs(root)
- return res

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

