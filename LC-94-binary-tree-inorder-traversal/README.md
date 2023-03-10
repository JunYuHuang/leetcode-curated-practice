# [LC 94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

## General Notes

- DFS inorder = L subtree -> root -> R subtree

## Solution 1: DFS recursive

- O(N) time and O(N) space solution
- optional: return empty array if null root
- empty res array
- helper recursive function inorder(curr)
  - if null curr, return
  - call itself on curr's L node
  - push curr's value to res array (process curr node)
    - don't need to check if curr is not null b/c already checked it in base case
  - call itself on curr's R node
- return res

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
