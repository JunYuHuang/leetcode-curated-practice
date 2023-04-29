# [LC 131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

## General Notes

- PEDAC: Problem
  - input: 
    - `s`: string of only lowercase alphabetical letters and of size in the range \[1, 16]
  - output: 
    - array of string arrays where each subarray:
      - whose total length of all its elements sum up to `s`'s length
      - whose element is a palindrome created from `s`
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(N * 2^N) T and O(N) S solution
- initialise empty `res` array
- helper function `isPali(l, r)`
  - returns true if substring\[l:r + 1] is a palindrome else false
- recursive helper `backtrack(curr, l)`:
  - if `l` is out of bounds
    - push copy of `curr` to `res` and return
  - loop for `r` in range \[l, len(s)]:
    - if `s[l:r + 1]` is a palindrome
      - push `s[l:r + 1]` to `curr`
      - `backtrack(curr, r + 1)`
      - pop from `curr`
- `backtrack([], 0)`
- return `res`