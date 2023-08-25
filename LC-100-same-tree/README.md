# [LC 100. Same Tree](https://leetcode.com/problems/same-tree/)

## General Notes

- PEDAC: Problem
  - input:
    - `p`: root of a binary tree, possibly null
      - if not null, the binary tree
        - has at most 100 nodes
        - has nodes with values in the range \[-10^4, 10^4]
    - `q`: root of another binary tree, possibly null
      - if not null, the binary tree
        - has at most 100 nodes
        - has nodes with values in the range \[-10^4, 10^4]
  - output:
    - `res`: boolean that is true if `p` and `q` are the same else false
  - `p` & `q` are the same IFF:
    - they have the same number of nodes
    - they are structurally identical
    - the nodes from each tree have the same matching values
- PEDAC: Examples
  - null `p` & null `q` -> true
  - non-null `p` & null `q` -> false
  - null `p` & non-null `q` -> false

## Solution 1 - DFS recursive

- O(N) T and O(N) S solution
- make function recursive
- return true if both `p` and `q` are null
- return false if either `p` or `q` are null
- return false if `p.val` is not equal to `q.val`
- `left` = `isSameTree(p.left, q.left)`
- `right` = `isSameTree(p.right, q.right)`
- return true if both `left` and `right` are true else false

## Solution 2: iterative (LC Official)

- O(N) T and O(N) S solution
- converts solution 1 recursive into an iterative function
- replace implicit call stack of recusive calls with queue of - elements [`p`-node, `q`-node]
- process queue while it is not empty and initialise it with - element [p, q]
  - if `isSame(p, q)` returns false, return false
- define helper `isSame(p, q)` function that checks if two nodes are the same
- if finished processing queue, return true
