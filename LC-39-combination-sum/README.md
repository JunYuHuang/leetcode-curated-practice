# [LC 39. Combination Sum](https://leetcode.com/problems/combination-sum/)

## General Notes

- PEDAC: Problem
  - input:
    - `candidates`: int array
      - of size in range \[1, 30]
      - of unique values `candidates[i]` in range \[2, 40]
    - `target`: int
      - of a value in range \[1, 40]
  - output:
    - `res`: int 2D array
      - of size in range \[0, 150]
      - of all possible unique int subarrays that each sum up to `target`
        - each subarray's size is in range `[1, candidates.length]`
    - empty if there is no valid combination
    - each combination can reuse the same int el from `candidates` any number of times
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(N \* 2^N) T and O(N \* 2^N) S solution
- summary
  - for each element in `candidates`, create 2 branches
    - branch 1: include `candidates[i]`
    - branch 2: exclude `candidates[i]`
- initialise variables
  - `res`: 2D array to hold all unique subset combos
  - `CANDIDATES_LEN`: int count of all elements in `candidates`
- create helper function `backtrack(i, curSub, curSum)`
  - if `i` >= `CANDIDATES_LEN` or `curSum` < 0,
    - return
  - if `curSum` == 0,
    - push `curSub` to `res`
    - return
  - include `candidates[i]` in recursive call
    - push `candidates[i]` to `curSub`
    - `dfs(i, curSub, curSum - candidates[i])`
  - exclude `candidates[i]` in recursive call
    - pop from `curSub`
    - `dfs(i + 1, curSub, curSum)`
- `dfs(0, [], tafget)`
- return `res`
