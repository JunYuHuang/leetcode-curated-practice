# [LC 78. Subsets](https://leetcode.com/problems/subsets/)

## General Notes

- PEDAC: Problem
  - input: 
    - `nums`: int array of size in range \[1, 10] whose values are in range \[-10, 10] and whose values are all unique
  - output: int matrix of permutations (array of int arrays)
  - valid subset properties
    - ~ 2^n solutions given an input with n elements
    - for each el, have 2 choices -> pick or don't pick
- PEDAC: Examples
  - nums = `[1,2,3]`
    - 3 elements, 8 solutions
    - valid subset properties
      - of size in range \[0, 3]
      - no duplicate ints in it
      - order of ints of it doesn't make it unique
  - nums = `[0]`
    - 1 element, 2 solutions
  - nums = `[0,1]`
    - 2 elements, 4 solutions
    - output = `[[],[0],[1],[0,1]]`

## Solution 1: recursive backtracking (NeetCode's modded)

- O(N * 2^N) T & and O(N * 2^N) S solution
- initialise empty res array
- define helper recursive function `backtrack(curr, i)`
  - if i is out of bounds
    - add copy of curr to res and return
  - push `nums[i]` to curr
  - call itself recursively on (curr, i + 1)
  - pop from curr
  - call itself recursively on (curr, i + 1) ?
- call backtrack([], i) and return res