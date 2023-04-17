# [LC 17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

## General Notes

- PEDAC: Problem
  - input: 
    - `digits`: string consisting only of chars `2-9` of length \[1, 4]
  - output: string array of all possible combinations that the number string can represent
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(N * 4^N) T & and O(N * 4^N) S solution
- initialise empty res array
- initialise digitToLetters hashmap that maps each valid digit char to its associated group of alpha char letters
- helper recursive function `backtrack(curr, i)`
  - if i is out of bounds (of digits str),
    - push copy of curr (arr) converted to str to res and return
  - for each char in digitToLetters\[i]
    - append char to curr
    - backtrack(curr, i + 1)
    - pop from curr
- backtrack([], 0)
- return res