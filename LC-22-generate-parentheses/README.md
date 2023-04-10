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
      - not the first char of string
      - closed < open
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(4^N / sqrt(N)) T and O(4^N / sqrt(N)) S solution (Catalan number)
- initialise res empty array
- helper recursive function `backtrack(currArr, open, close)`
  - if length of currArr has reached n * 2, 
    - convert it to a string and push it to res
    - return
  - if open < n,
    - push open parentheses to currArr
    - call itself recursively on (currArr, open + 1)
    - pop from currArr
  - if open < close,
    - push closed parentheses to currArr
    - call itself recursively on (currArr, open, close + 1)
    - pop from currArr
- backtrack([], 0, 0)
- return res