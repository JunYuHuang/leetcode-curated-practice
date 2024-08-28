# [LC 17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## General Notes

- PEDAC: Problem
  - input:
    - `digits`: string
      - of chars from `2-9` only
      - of length in \[0, 4]
  - output:
    - `res`: string array of all possible combinations that `digits` can represent
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(N \* 4^N) T and O(N \* 4^N) S solution
- return empty array if `digits` is of length 0
- initialise variables
  - `digToChar`: hashmap that maps all valid string digits to a string of their associated alphabet chars
  - `res`: empty array
  - `N`: length of `digits`
- define helper function `dfs(i, comb)`
  - if `i` >= `N`
    - push `comb` converted to string to `res`
  - loop for each char `c` in `digToChar[digits[i]]`
    - push `c` to `comb`
    - `dfs(i + 1, comb)`
    - pop from `comb`
- `dfs(0, [])`
- return `res`
