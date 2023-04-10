# [LC 100. Same Tree](https://leetcode.com/problems/same-tree/)

## General Notes

- PEDAC: Problem
  - input: 
    - `p`: root of a binary tree, possibly null
    - `q`: root of another binary tree, possibly nll
  - output: 
    - boolean that indicates if `p` and `q` are the same
- PEDAC: Examples

## Solution 1: recursive (LC Official)

- O(N) T and O(N) S
- make function itself recursive
- if both `p` and `q` are null, return true
- if one of the nodes is null but the other is not, return false
- if both nodes are not null but have different values, return false
- return result of AND'd calls on itself to compare both `p`'s and `q`'s L and R children respectively

## Solution 2: iterative (LC Official)

- O(N) T and O(N) S
- converts solution 1 recursive into an iterative function
- replace implicit call stack of recusive calls with queue of elements \[`p`-node, `q`-node]
- process queue while it is not empty and initialise it with element \[`p`, `q`]
  - if `isSame(p, q)` returns false, return false
- define helper `isSame(p, q)` function that checks if two nodes are the same
- if finished processing queue, return true


