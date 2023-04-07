# [LC 37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)

## General Notes

- PEDAC: Problem
  - input: 
    - `board`: 9 * 9 matrix with values from set { 1-9, . }
  - output: 
    - none; modify matrix in-place
  - guaranteed `board` has only 1 solution
- PEDAC: Examples

## Solution 1: DFS backtracking ([msdn's modded](https://leetcode.com/problems/sudoku-solver/solution/1332635))

- O(9^M) T and O(81) S solution
- initialise class-level instance (global) variables
  - empty hashmaps of sets for cols, rows, squares
  - candidates string array for nums 1-9
- define below helper functions inside solveSudoku() function
- initialScan():
  - loop thru board and add pre-placed digits to their relevant rows, cols, squares sets
- canPlace(r, c, val):
  - returns true if val doesn't exist in the current row, col, or square
- placeNum(r, c, val):
  - sets val to the cell and marks it in the relevant 3 sets
- removeNum(r, c, val):
  - sets cell to empty val `.` and removes it from the relevant 3 sets
- getNextCell(r, c):
  - returns next-right cell in row or leftmost cell in next row
- recursive backtrack(r, c):
  - if went out-of-bounds on boards, return true
  - if current cell is already filled (i.e. is a digit),
    - return backtrack() on next cell
  - loop thru the candidates array
    - if canPlace() on the current cell,
      - placeNum()
      - if recursive call next cell returns true,
        - return true
      - removeNum()
- run initialScan() and call backtrack() on top-left cell of board