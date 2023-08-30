# [LC 572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root of a binary tree
      - guaranteed to be not null
      - the binary tree
        - has at most 2000 nodes
        - has nodes with values in the range \[-10^4, 10^4]
    - `subRoot`: root of another binary tree
      - guaranteed to be not null
      - the binary tree
        - has at most 2000 nodes
        - has nodes with values in the range \[-10^4, 10^4]
  - output:
    - `res`: boolean that is true if `subRoot` is a subtree of `root` else false
  - `subRoot` is a subtree of `root` IFF:
    - `subTree` is identical to `root`
      - same structure, same node count, same node values
    - `root` contains a node that is identical to `subRoot`
- PEDAC: Examples
  - TODO

## Solution 1 - DFS recursive + iterative

- O(N^2) T and O(N^2) S solution
- helper function `isSameTree(p, q)`
  - returns true if node `p` and node `q` are the same else false
  - return true if both `p` and `q` are null
  - return false if either `p` or `q` are null
  - return false if `p.val` != `q.val`
  - `isLeftSame` = `isSameTree(p.left, q.left)`
  - `isRightSame` = `isSameTree(p.right, q.right)`
  - return true if both `isLeftSame` and `isRightSame` are true else false
- traverse tree of `root` in with a queue
  - initialise `queue` with `root`
  - while `queue` is not empty,
    - `curr` = pop 1st element from `queue`
    - if `isSameTree(curr, subRoot)` returned true,
      - return true
  - if exited loop, return false

