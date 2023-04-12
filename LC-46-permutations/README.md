# [LC 46. Permutations](https://leetcode.com/problems/permutations/)

## General Notes

- PEDAC: Problem
  - input: 
    - `nums`: int array of size in range \[1, 6] whose values are in range \[-10, 10] and whose values are all unique
  - output: int matrix of permutations (array of int arrays)
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's)

- O(N * N!) T & and O(N * N!) S solution
- make function itself `permute(nums)` recursive
- initialise empty res array
- if nums is of 1 el, return a copy of it in an empty array
- loop thru each int in nums
  - pop and store first el in nums in `n`
  - store recursive call of itself in `perms`
  - for each perm in `perms`, push `n` to it
  - add the perms to res
  - push `n` back to nums
- return res