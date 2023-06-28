# [LC 74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

## General Notes

- PEDAC: Problem
  - input:
    - `matrix`: int matrix
      - each row is sorted in non-decreasing order
      - 1st int of each row > last int of prev row
      - `matrix`'s size is in range \[1, 100]
      - `matrix[i]`'s (col) is in range \[1, 100]
      - each value (`matrix[i][j]`) is in range \[-10^4, 10^4]
      - may contain duplicate values
    - `target`: int that may or may not be in `matrix`
      - of values in range \[-10^4, 10^4]
  - output:
    - `res`: boolean that represents if `target` is in `matrix` (true) or not (false)
  - constraints
    - algorithm must have a `O(Log(M * N))` runtime complexity
  - return false if `target` < `matrix[0][0]` or `target` > `matrix[-1][-1]`
  - found correct row `matrix[r]` if:
    - `target` >= `matrix[r][0]` AND `target` <= `matrix[r][-1]`
  - found correct col `matrix[r][c]` if:
    - `target` == `matrix[r][c]`
- PEDAC: Examples

## Solution 1: binary search

- O(Log(M * N)) T and O(1) S solution
- summary
  - find which row `target` is in with binary search
  - find the `target`'s col in the row with binary search
- initialise variables
  - `ROWS`: int set to size of `matrix`
  - `COLS`: inset to size of `matrix[0]`
  - `top`: int set to 0 that represents the 'left' pointer for `matrix`
  - `bot`: int set to `ROWS` - 1 that represents the 'right' pointer for `matrix`
  - `left`: int set to 0 that represents the left pointer of a row `matrix[i]`
  - `right`: int set to `COLS` - 1 that represents the right pointer of a row `matrix[i]`
- return false if `target` < `matrix[0][0]` or `target` > `matrix[-1][-1]`
- `midRow` = 0
- while `top` <= `bot`
  - `midRow` = (`top` + `bot`) // 2
  - if `target` < `matrix[midRow][0]`:
    - `bot` = `midRow` - 1
  - else if `target` > `matrix[midRow][-1]`:
    - `top` = `midRow` + 1
  - else (`target` >= `matrix[midRow][0]` AND `target` <= `matrix[midRow][-1]`)
    - break out of loop
- while `left` <= `right`
  - `midCol` = (`left` + `right`) // 2
  - if `target` == `matrix[midRow][midCol]`
    - return true
  - else if `target` < `matrix[midRow][midCol]`
    - `right` = `midCol` - 1
  - else (`target` > `matrix[midRow][midCol]`)
    - `left` = `midCol` + 1
- return false
