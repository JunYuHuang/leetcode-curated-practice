# [LC 79. Word Search](https://leetcode.com/problems/word-search/)

## General Notes

- PEDAC: Problem
  - input:
    - `board`: a 2D array of string subarrays
      - a `m x n` matrix of alphabetical string characters
      - `m`, `n`: ints in range \[1, 6]
      - `m`: count of rows
      - `n`: count cols
      - has `m` string subarrays
      - each subarray has `n` elements
      - each subarray `board[m]` only has lower and upper case English letter strings / chars
    - `word`: a string of alphabetical characters of size in range \[1, 15]
      - of only lower and upper case English letter strings / chars
      - if in `board`,
        - of cells `board[m][n]`
          - that are directly horizontally or vertically adjacent
          - that can only each be used once
  - output:
    - boolean that indicates if `word` exists inside `board` or not
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(4^L \* M \* N) T and O(4^L \* M \* N) S solution
- initialise variables
  - `ROWS`: length of `board`
  - `COLS`: length of `board[0]`
  - `WORD_LEN`: length of `word`
  - `directions`: array of 2-sized int arrays that represent the perpendicular adjacent neighbouring cells `row, col` diffs of a cell
- if `word` is longer than all cells in `board`,
  - return false
- loop thru every row `r` and col `c` in `board`,
  - continue if `board[r][c]` is not `word`'s first char
  - if `dfs(r, c, 0, empty set)` returns true,
    - return true
- return false
- helper recursive function `dfs(r, c, i, used)`
  - if `i` is out-of-bounds for `word`,
    - return true
  - if `r, c` is out-of-bounds, not equal to `word[i]`, or visited in `used`,
    - return false
  - add `r, c` to `used`
  - loop thru every 4 neighboring cell `nei_r, nei_c` of the cell `r, c`
    - if `dfs(nei_r, nei_c, i + 1, used)` returns true,
      - return true
  - remove `r, c` from `used`
  - return false
