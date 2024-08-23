# [LC 77. Combinations](https://leetcode.com/problems/combinations/)

## General Notes

- PEDAC: Problem
  - input:
    - `n`: int in range \[1, 20]
      - the inclusive upper bound of the range of numbers
    - `k`: int in range \[1, `n`]
      - length of each int subarray or set in the results
  - output:
    - `res`: 2D array of int arrays
- PEDAC: Examples

## Solution 1: DFS backtracking (NeetCode's expl.)

- O(k \* n^k) T and O(k \* n^k) S solution
- initialise variables
  - `res`: empty 2D array
- define helper function `dfs(i = 1, comb = [])`
  - if `comb.length` == `k`,
    - push copy of `comb` to `res`
    - return
  - loop for `j` in range \[`i`, `n`],
    - push `j` to `comb`
    - `dfs(j + 1, comb)`
    - pop from `comb`
- `dfs()`
- return `res`
