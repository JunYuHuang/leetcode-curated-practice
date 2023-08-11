# [LC 104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a binary tree
      - may be null
      - if not null, has a value in the range \[-100, 100]
    - binary tree whose root node is `root`
      - has nodes in the range \[0, 10^4]
      - has nodes whose values are in the range \[-100, 100]
  - output:
    - `res`: int that represents the max depth of the tree whose root node is `root`
      - in the range \[0, 10^4]
  - depth = level + 1
    - null root has depth 0
    - root with no children has depth 1
- PEDAC: Examples
  - TODO

## Solution 1: BFS iterative

- O(N) time and O(N) space solution
- traverse tree in a level-order manner using queue and increment depth for every level traversed
- initialise variables
  - `res`: int that represents the max depth set to 0 initially
  - `queue`: queue array for traversing the tree in BFS order
- if `root` is not null, push it to `queue`
- while `queue` is not empty
  - `res++`
  - `levelSize` = length of `queue`
  - loop for `i` for the range [0, `levelSize` - 1]
    - `curr` = pop first element from `queue`
    - skip to next iteration if `curr` is null
    - push `curr.left` to `queue` if `curr.left` is not null
    - push `curr.right` to `queue` if `curr.right` is not null
- return `res`

## Solution 2: DFS recursive bot-up

- O(N) time and O(N) space solution
- make function itself recursive
- base case: depth of current node is 0 if node is null
- return max() of calling itself on current node's L and R children + 1

## Solution 3: DFS recursive bot-up

- O(N) time and O(N) space solution
- similar approach to solution 2 DFS recursive bot-up but
  - global res int var initialised to 0
  - non-pure helper recursive function dfs(curr, depth)
    - returns if curr is null
    - update res only if curr is a leaf node
    - calls itself on curr's children with depth incremented

## Solution 4: DFS iterative (NeetCode's modified)

- O(N) time and O(N) space solution
- traverse tree in preorder using stack of (node, depth) elements
- optional: return 0 if null root
- initialise res int to 0, stack with (root, 1 or (1 if root is not null else 0))
- while stack is not empty
  - curr, depth = pop from stack top
  - if curr is not null
    - if depth > res, update res
    - push curr's non-null children (R then L) to stack with depth++
- return res
