# [LC 112. Path Sum](https://leetcode.com/problems/path-sum/)

## General Notes:

- PEDAC: Problem
  - input:
    - `root`: TreeNode root of a binary tree
      - may be null
      - whose binary tree
        - has nodes in the range \[0, 5000]
        - has nodes of values in the range \[-1000, 1000]
    - `targetSum`: int in range \[-1000, 1000]
  - output:
    - `res`: bool that is true if there exists a root-to-leaf path whose sum of its nodes equals `targetSum` else false
  - for every path traversed,
    - must start from the root node and end at a leaf node
    - leaf node is a node with no L or R children
    - only need 1 path to return true to return true for the function
- PEDAC: Examples
  - null root
    - return false
  - tree with only positive nodes and has one path = targetSum
    - return true
- PEDAC: DS&A

## Solution 1: DFS recursive

- O(N) T and O(N) S solution
- summary
  - make `hasPathSum(root, targetSum)` method itself recursive
    - if `root` is null, return false
    - `currSum` = `targetSum` - `root.val`
    - if `currSum` is 0 and `root` is a leaf node,
      - return true
    - return `hasPathSum(root.left, currSum)` or `hasPathSum(root.right, currSum)`

## Solution 2: DFS iterative

- O(N) time and O(N) space solution
- same approach as solution 1 DFS recursive but
  - replace recursive calls with explicit stack of elements of recursive call parameters
- optional: return false if root is null
- initialise stack with pair (root, targetSum)
- while stack is not empty:
  - node, currSum = pop from stack top
  - if node is null, skip to next loop
  - res int = currSum - node's value
  - if node is leaf node and res is 0, return true
  - push pairs (node.L, res), (node.R, res) to stack
- if finished processing tree, return false
