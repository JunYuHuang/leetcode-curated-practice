# [LC 230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a BST
      - guaranteed to be non-null
      - whose BST
        - has nodes in the range \[1, 10^4]
        - has nodes with values in the range \[0, 10^4]
        - has nodes with possible duplicate values
  - output:
    - `res`: represents the `k`th smallest 1-indexed value of all the values of the nodes in the tree
- PEDAC: Examples
  - TODO

## Solution 1: DFS inorder recursive

- O(N) T and O(N) S solution
- initialise variables
  - `visited`: empty int array that represents the order of the values of the nodes in the BST whose root node is `root` visited
- define helper function `inorder(curr)`
  - return if `curr` is null
  - `inorder(curr.left)`
  - push `curr.val` to `visited`
  - `inorder(curr.right)`
- `inorder(root)`
- return `visited[k - 1]`

## Solution 2: DFS inorder recursive optimized (tmohan's modded)

- O(LogN) T and O(LogN) S solution
- same approach as solution 1 but
  - use `res` variable to store an int instead of an array
  - recursive helper function exits early when `k` elements have been visited
