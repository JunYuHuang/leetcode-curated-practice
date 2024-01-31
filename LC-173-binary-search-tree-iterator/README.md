# [LC 173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/)

## General Notes

- PEDAC: Problem
  - design `BSTIterator` class with the following methods:
    - `constructor(root)`
      - input(s):
        - `root`: TreeNode guaranteed to not be null
      - initialises a pointer to some non-existent int smaller than any node in the BST
    - `next()`
      - input(s): none
      - moves the pointer to the right
      - output(s):
        - `res`: int value of node that the pointer points to
    - `hasNext()`
      - input(s): none
      - output(s):
        - `res`: boolean that is true if there is a number to the right of the pointer else false
  - constraints
    - `next()` calls are guaranteed to be valid
    - BST has int values in the range \[0, 10^6]
    - BST has nodes in range \[1, 10^5]
  - follow up
    - make `next()` run in O(1) time and use O(H) memory
    - make `hasNext()` run in O(1) time and use O(H) memory
  - DFS inorder = L subtree -> root -> R subtree
- PEDAC: Examples
  - TODO

## Solution 1: array brute force

- method dependent T and S solution
- summary:
  - entirely ignore BST property of tree
  - set class instance variables
    - `inorder`: int array that is initially empty that represents the values of each node in the BST traversed in inorder with a dummy value as its first value
    - `pos`: int set to -1 that represents the current index pointer in `inorder`
  - `constructor(root)`
    - traverses BST recursively in DFS inorder to build `inorder`
  - `next()`
    - increments `pos` by 1
    - returns `inorder[pos]`
  - `hasNext()`
    - returns `pos + 1` < size of `inorder`

## Solution 2: DFS iterative (NeetCode's modded)

- method dependent T and S solution
- summary:
  - simulate implicit call stack with explicit stack of `TreeNode`s
  - `constructor(root)`
    - start at `root`
    - keep pushing nodes to stack and going down left in tree while `curr` node is not null
  - `next()`
    - `res` = pop node from stack
    - `curr` = `res.right`
    - keep pushing `curr` to stack and moving `curr` down its left tree while `curr` is not null
    - return `res.val`
  - `hasNext()`
    - returns true if stack is not empty else false
