# [LC 52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)

## General Notes

- PEDAC: Problem
  - input: 
    - `n`: int in range \[1, 9]
  - output: 
    - int that represents the count of all possible unique solutions
- PEDAC: Examples

## Solution 1: DFS backtracking (NeetCode's modded)

- O(N! * N)? time and O(N^2) space solution
- initialise variables
  - res = int set to 0 that will be the returned count result
  - empty sets for col, posDiag (r + c), negDiag (r - c) that track if a queen has been placed on such a dimension / position
- don't need to have set for row b/c it's recursive function will place 1 queen on every row
- helper recursive function backtrack(r):
  - if reached last row, res++
  - loop thru each col from to 0 to n - 1
    - if a queen and its attack vector does not occupy the current cell's col, posDiag, or negDiag
      - place a queen there by adding its relevant coordinates to the col, negDiag, posDiag sets
      - call recursively on backtrack(r + 1)
      - remove a queen there by removing its relevant coordinates from the col, negDiag, posDiag sets
- call backtrack(0)
- return res