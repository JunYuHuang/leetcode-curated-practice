# [LC 36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

## General Notes

- PEDAC: Problem
  - input:
    - `board`: 9 * 9 matrix with strings from set { 1-9, . }
  - output:
    - boolean that indicates if `board` is a valid sudoku board or not
  - valid if
    - each row has string digits `1-9` with no duplicates
    - each col has string digits `1-9` with no duplciates
    - each `3 x 3` sub-boxes has string digits `1-9` with no duplicates
  - constraints
    - valid board may not be solvable
    - only filled cells need to be validated according to rules
- PEDAC: Examples

## Solution 1: hashset solution (NeetCode's modded)

- O(9^2) T and O(9^2) S solution
- initialise variables
  - `rows`: hashmap that maps each row index to a string set containing all the digits in that row
  - `cols`: hashmap that maps each row index to a string set containing all the digits in that col
  - `box`: hashmap that contains maps each sub-box of the grid to a string set containing all the digits in that sub-box
    - key = tuple pair of (row_index / 3 as int, col_index / 3 as int)
- iterate thru `board` with nested for loops
  - if the current cell is a `.` char, continue
  - if the current cell (which is a digit) is in any of the respective sets of the following hashmaps, return false:
    - `rows[r]`
    - `cols[c]`
    - `box[(r // 3, c // 3)]`
  - add the current cell to the above sets of the following hashmaps
- if exited loop, return true
