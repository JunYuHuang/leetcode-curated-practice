# [LC 79. Word Search](https://leetcode.com/problems/word-search/)

## General Notes

- PEDAC: Problem
  - input: 
    - `board`: a `m x n` matrix of alphabetical string characters
    - `m`, `n`: ints in range \[1, 6]
    - `word`: a string of alphabetical characters of size in range \[1, 15]
  - output: 
    - boolean that indicates if `word` exists inside `board` or not
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(M * N * 4^K) T and O(M * N * 4^K) S solution
- initialise ROWS = len(board), COLS = len(board[0])
- if size of `word` < `board`'s area, return false
- initialise empty visit set
- backtrack(i, r, c):
  - if i == len(word), return true
    - b/c means we reached end of word
  - if cell is invalid, return false
    - cell is invalid if any of the following are true:
      - r or c is out of bounds
      - cell is not equal to the current char in `word
      - (r, c) has been visited
  - add cell (r, c) to visit set
  - for 4 adj./neigbour cells of current cell (r, c):
      - if backtrack(i + 1, adjR, adjC), return true
  - remove cell (r, c) from visit set
  - return false
- loop over `board`'s cells (via rows and cols)
  - if cell != 1st char of `word`: continue
  - if `backtrack(i, r, c)`, return true
- if exited loop, return false