# [LC 47. Permutations II](https://leetcode.com/problems/permutations-ii/)

## General Notes

- PEDAC: Problem
  - input: 
    - `nums`: int array of size in range \[1, 8] whose values are in range \[-10, 10] and may have duplicates
  - output: 
    - int matrix of permutations (array of int arrays)
      - each perm is of size N
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(N * N!)? T & and O(N * N!) S solution
- initialise empty `res` array
- build `nToCount` hashmap that maps each unique int in `nums` to how many times it occurs
- helper recursive function `backtrack(perm)`
  - if perm reaches size N, push copy of it to res and return
  - loop thru each int key in `nToCount`
    - if `nToCount[n]` > 0,
      - push `n` to `perm` and decrement `nToCount[n]`
      - backtrack(perm)
      - pop from `perm` and increment `nToCount[n]`
- backtrack([])
- return res