# [LC 90. Subsets II](https://leetcode.com/problems/subsets-ii/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: non-empty int array
      - of size in range \[1, 10]
      - of values in range \[-10, 10]
  - output:
    - `res`: 2D array of int subarrays that represent all possible unique subsets (power set)
      - order of subarrays doesn't matter
      - size ranges from 0 to N
      - order of ints in a subarray doesn't matter (we look for combinations not permutations)
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's expl.)

- O(N \* 2^N) T and O(N \* 2^N) S solution
- summary
  - same approach as Subsets I but
    - sort input array `nums`
    - including an element `nums[i]` from backtracking is the same
    - excluding an element `nums[i]` from backtrack must also skip duplicates of `nums[i]`
      - use loop to move index `i` until `i` is out of bounds or `nums[i]` is not at a duplicate
- sort `nums` in ASC order
- initialise variables
  - `res`: empty 2D array
  - `N`: length of `nums`
- define helper function `dfs(i, sub)`
  - if `i` >= `N`,
    - push copy of `sub` to `res`
    - return
  - include `nums[i]` in `sub`
    - push `nums[i]` to `sub`
    - `dfs(i + 1, sub)`
  - exclude `nums[i]` and its dupes from `sub`
    - pop from `nums[i]`
    - while `i + 1` < `N` and `nums[i]` == `nums[i + 1]`,
      - `i++`
    - `dfs(i + 1, sub)`
- `dfs(0, [])`
- return `res`
