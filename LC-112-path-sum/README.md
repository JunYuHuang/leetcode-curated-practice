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
- define a helper function `dfs(node, curSum)`
  - return false if `node` is null
  - `curSum` -= `node.val`
  - if `node` is a leaf node,
    - return `curSum` == 0
  - `leftCall` = `dfs(node.left, curSum)`
  - `rightCall` = `dfs(node.right, curSum)`
  - return `leftCall` || `rightCall`
- return `dfs(root, targetSum)`

## Solution 2: DFS iterative

- O(N) time and O(N) space solution
- same approach as solution 1 DFS recursive but
  - simulate call stack with an explicit stack
- initialise variables
  - `stack`: stack of `[node, curSum]` elements initialised with element `[root, targetSum]`
    - only holds non-null nodes
- return false if `node` is null
- while `stack` is not empty,
  - `node`, `curSum` = pop last el from `stack`
  - `curSum` -= `node.val`
  - if `node` is a leaf node and `curSum` is 0,
    - means both `node.left` and `node.right` are null
    - return true
  - if `node.left`,
    - push `[node.left, curSum]` to `stack`
  - if `node.right`,
    - push `[node.right, curSum]` to `stack`
- return false if exited loop
