# [LC 22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

## General Notes

- PEDAC: Problem
  - input:
    - `n`: int in range \[1, 8] representing the number of parentheses pairs
  - output: string array representing all combinations of well-formed parentheses
  - for each combination string,
    - open = # of open parentheses in combo string
    - close = # of closed parentheses in combo string
    - length must be n * 2
    - can append open parentheses `(` only if
      - first char of string
      - not the last char of string
      - open < n
    - can append closed parentheses `)` only if
      - there is at least 1 open parentheses
      - last char of string
      - not the first char of string
      - closed < open
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(4^N / sqrt(N)) T and O(4^N / sqrt(N)) S solution (Catalan number)
- initialise empty `res` array
- recursive function `backtrack(comb, open, closed)`
  - if either `open` > `n` or `closed` > `n` (optional)
    - return
  - if both `open` and `closed` equal to `n`
    - push `comb` converted to a string to `res`
    - return
  - if `open` < `n`
    - push a `(` char to `comb`
    - call `backtrack(comb, open + 1, closed)`
    - pop from `comb`
  - if `closed` < `open`
    - push a `)` char to `comb`
    - call `backtrack(comb, open, closed + 1)`
    - pop from `comb`
- call `backtrack([], 0, 0)`
- return `res`
