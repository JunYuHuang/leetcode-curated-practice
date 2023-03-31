# [LC 240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)

## General Notes

- PEDAC: Problem
  - input: 
    - `matrix`: a m x n integer 2D array sorted in a certain way
      - guranteed to be at least of size 1 x 1
    - `target`: int that may or may not be in `matrix`
  - output: boolean to indicate if `target` is in `matrix` or not
  - 
- PEDAC: Examples

## Solution 1: iterative D&C (DBabichev's modded)

- O(M + N) time and O(1) space solution
- can start from top-right corner cell (this solution) OR
bottom-left corner cell
- initialise variables
  - row = initialised to first row index in matrix
  - col = initialised to last col index in matrix
- while row and col indices are in-bounds
  - if cell (row, col) > target, 
    - move to next left column (col--)
    - all ints below cell are greater than it, so disregard this col
  - else if cell (row, col) < target,
    - move to next row down (row++)
    - all ints left of cell in current row < target and all ints right of cell in current row > target, so disregard this row
  - else return true
    - b/c cell (row, col) in matrix equals target
- if exited loop, return false