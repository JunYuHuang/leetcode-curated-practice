# [LC 47. Permutations II](https://leetcode.com/problems/permutations-ii/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in range \[1, 8]
      - of values in range \[-10, 10]
      - may have duplicates
  - output:
    - `res`: array of int arrays
      - each int array is a perm
      - each int array is of size `nums.length`
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(N \* N!) T and O(N \* N!) S solution
- initialise variables
  - `count`: hashmap that maps each unique int to its occurrences in `nums`
  - `res`: empty array
  - `N`: length of `nums`
- define helper function `dfs(perm)`
  - if length of `perm` >= `N`,
    - push copy of `perm` to `res`
    - return
  - loop thru every key `n` in `count`,
    - if `n`'s value > 0,
      - push `n` to `perm`
      - `count[n]--`
      - `dfs(perm)`
      - pop from `perm`
      - `count[n]++`
- `dfs([])`
- return `res`
