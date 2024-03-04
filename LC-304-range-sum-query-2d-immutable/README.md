# [LC 304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)

## General Notes:

- PEDAC: Problem
  - class methods and inputs
    - `NumMatrix(matrix)` constructor
      - input: 2D int array `nums`
      - output: a `NumMatrix` object
    - `sumRegion(row1, col1, row2, col2)` method
      - input: int `row1`, int `col1`, int `row2`, int `col2`
      - output: an int `res` equal to the sum of all ints from `matrix` in the rectange having upper left corner `(row1, col1)` and lower right corner `(row2, col2)`
  - constraints
    - `sumRegion()` must run in O(1) time
    - `matrix`: a 2D int array
      - has `m` rows in the range \[1, 200]
      - has `n` cols in the range \[1, 200]
      - `matrix[i][j]` is an int in the range \[-10^4, 10^4]
      - `row1`: an int in the range \[0, `row2`]
      - `row2`: an int in the range \[`row1`, `m`]
      - `cow1`: an int in the range \[0, `cow2`]
      - `cow2`: an int in the range \[`cow1`, `n`]
    - 10^4 max calls made to `sumRegion()`
- PEDAC: Examples
- PEDAC: DS&A

## Solution 1: summed area table (Wikipedia modded)

- O(1) T `sumRegion()`
- `NumMatrix(matrix)` constructor
  - precompute the summed area table `sumMatrix` as an instance field
  - `sumMatrix`: int matrix of same rows and cols as `matrix`
    - initialised with all 0's
  - loop over `sumMatrix` and update its values
    - `sumMatrix[x][y]` = `matrix[x][y]` + `sumMatrix[x][y - 1]` + `sumMatrix[x - 1][y]` - `sumMatrix[x - 1][y - 1]`
    - if `y` <= 0,
      - use 0 instead of `sumMatrix[x][y - 1]`
    - if `x` <= 0,
      - use 0 instead of `sumMatrix[x - 1][y]`
    - if both `x` and `y` are <= 0,
      - use 0 instead of `sumMatrix[x - 1][y - 1]`
- `sumRegion(row1, col1, row2, col2)` method
  - translate `A - B - C + D` sum method by in terms of `sumMatrix` where:
    - points A thru D represent a rectangular area in `matrix`
    - `A`: top-left corner
    - `B`: top-right corner
    - `C`: bot-left corner
    - `D`: bot-right corner
  - `topLeft`: `sumMatrix[row1 - 1][col1 - 1]` if both `row1` and `col1` > 0 else 0
  - `topRight`: `sumMatrix[row1 - 1][col2]` if `row1` > 0 else 0
  - `botLeft`: `sumMatrix[row2][col1 - 1]` if `col1` > 0 else 0
  - `botRight`: `sumMatrix[row2][col2]`
  - return `topLeft` - `topRight` - `botLeft` + `botRight`

## Solution 2: prefix sums (NeetCode's modded)

- O(1) T `sumRegion()`
- summary
  - same approach as solution 1 but `sumMatrix` uses an extra row and column
    - i.e. if `matrix` has `m` rows and `n` cols, then `sumMatrix` has `m` + 1 rows and `n` + 1 cols
- `NumMatrix(matrix)` constructor
  - initialise `sumMat` int matrix with `m + 1` rows and `n + 1` cols based on `matrix`
  - loop for `r` rows from indices 1 to `m + 1`,
    - loop for `c` cols from indices 1 to `n + 1`,
      - `downleft`: `sumMat[r][c - 1]`
      - `upRight`: `sumMat[r - 1][c]`
      - `upLeft`: `sumMat[r - 1][c - 1]`
      - `downRight`: `matrix[r - 1][c - 1]`
      - `sumMat[r][c]` = `downRight` + `downLeft` + `upRight` - `upLeft`
- `sumRegion(row1, col1, row2, col2)` method
  - note: must add an extra +1 offset to all row and col indices to account for extra row and col in `sumMat`
    - `row1` += 1, `col1` += 1, `row2` += 1, `col2` += 1
  - `topLeft`: `sumMat[row1 - 1][col1 - 1]`
  - `topRight`: `sumMat[row1 - 1][col2]`
  - `botLeft`: `sumMat[row2][col1 - 1]`
  - `botRight`: `sumMat[row2][col2]`
  - return `botRight` - `botLeft` - `topRight` + `topLeft`
