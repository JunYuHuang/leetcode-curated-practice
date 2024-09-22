# [LC 40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

## General Notes

- PEDAC: Problem
  - input:
    - `candidates`: int array
      - of size in range \[1, 100]
      - of values in range \[1, 50]
      - may have duplicate values
    - `target`: int
      - of value in range \[1, 30]
  - output:
    - `res`: array of int arrays
      - each subarray
        - represents all unique combos whose ints sum up to `target`
        - uses each int from `candidate` only once
        - no duplicates
        - order doesn't matter
        - of size in range \[1, N]
      - order of subarrays doesn't matter
  - backtrack(curr, i) helper function
    - return if i is out of bounds or sum(curr) > target
    - keep adding elements if sum(curr) < target
    - found solution if i is in bounds and sum(curr) == target
    - how to guarantee solutions in res array are unique combinations?
      - sort input array `candidates` and when excluding an el skip to next diff el
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's expl.)

- O(N \* 2^N) T and O(N \* 2^N) S solution
- initiallise variables
  - `N`: length of `candidates`
  - `res`: empty array
- sort `candidates` in ASC order
- define helper function `dfs(i, comb, curSum)`
  - if `curSum` is 0,
    - add copy of `comb` to `res`
    - return
  - if `i` is out-of-bounds or `curSum` is negative,
    - return
  - recursive call branch: include `candidates[i]`
    - push `candidates[i]` to `comb`
    - `dfs(i + 1, comb, curSum - candidates[i])`
    - pop from `comb`
  - recursive call branch: exclude `candidates[i]` and its dupes
    - increment `i` while `candidates[i]` equals `candidates[i + 1]`
    - `dfs(i + 1, comb, curSum)`
- `dfs(0, [], target)`
- return `res`
