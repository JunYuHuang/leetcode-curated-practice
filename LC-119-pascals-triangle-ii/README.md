# [LC 119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

## General Notes

- PEDAC: Problem
  - input: int rowIndex in range [0, 33]
  - ouput: array of ints equal to the ints in the row `rowIndex` (0-indexed)
  - follow-up: only use O(`rowIndex`) extra space to complete problem
  - recurrence relation for each cell in Pascal's triangle
    - f (i, j) = f (i - 1, j - 1) + f (i - 1, j)
    - f (i, j) = 1 where j = 1 or j = i
  - observations
    - row i has i + 1 elements
    - the elements in each row form a palindrome in order
- PEDAC: Examples
  - row 0: 1
  - row 1: 1, 1
  - row 2: 1, 2, 1
  - row 3: 1, 3, 3, 1
  - row 4: 1, 4, 6, 4, 1

## Solution 1: iterative

- O(N^2) time and O(rowIndex)? space solution
- initialise res array with \[1]
- loop for r range [1, rowIndex + 1) times
  - initialise temp array of all 1's for size res + 1
  - for c in range [1, len(temp) - 1)
    - temp\[c] = res\[c - 1] + res\[c]
  - assign res to temp
- return res

## Solution 2: recursive (chetan_6780's modded)

- O(N^2) time and O(N) space solution
- same approach as solution 1 but make the function recursive
  - base case = return \[1] if rowIndex is 0
  - initialise currRow array with \[1]
  - get prevRow from recursive call on (rowIndex - 1)
  - for i, loop thru currRow from 2nd el (1) to 2nd last el (before rowIndex)
    - push prevRow\[i - 1] + prevRow\[i] to currRow
  - push 1 to currRow
  - return currRow