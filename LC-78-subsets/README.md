# [LC 78. Subsets](https://leetcode.com/problems/subsets/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: non-empty int array
      - of size in range \[1, 10]
      - of values are in range \[-10, 10] and are all unique
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

- O(N \* 2^N) T and O(N \* 2^N) S solution
- initialise variables
  - `res`: empty array to hold all unique subsets of `nums`
  - `NUMS_LEN`: int count of all elements in `nums`
- define helper function `dfs(i, subset)`
  - if `i` is out-of-bounds,
    - means `i` >= `NUMS_LEN`
    - push a copy of `subset` to `res`
    - return
  - push `nums[i]` to `subset`
  - `dfs(i + 1, subset)`
  - pop from `subset`
  - `dfs(i + 1, subset)`
- `dfs(0, [])`
- return `res`
