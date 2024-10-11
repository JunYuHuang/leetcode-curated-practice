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
  - '23'
    - 'a'
      - 'd'
      - 'e'
      - 'f'
    - 'b'
      - 'd'
      - 'e'
      - 'f' -> 'bf'
  - ''
    - -> []

## Solution 1: recursive backtracking (NeetCode's modded)

- O(4^N \* N) T and O(4^N \* N) S solution
- if `digits` is empty string,
  - return empty array
- set variables
  - `digToChars`: hashmap that maps each numerical digit `2-9` to a string of alpha chars associated with it
  - `res`: empty array
- define helper function `dfs(i, comb)`
  - if `i` is out-of-bounds,
    - push `comb` as string to `res`
    - return
  - for each char `char` in the value mapped to key `digits[i]` in `digToChars`,
    - push `char` to `comb`
    - `dfs(i + 1, comb)`
    - pop from `comb`
- `dfs(0, [])`
- return `res`
