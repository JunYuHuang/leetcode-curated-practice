# [LC 39. Combination Sum](https://leetcode.com/problems/combination-sum/)

## General Notes

- PEDAC: Problem
  - input: 
    - `candidates`: int array of distinct els of size in range \[2, 30] and whose values are in range \[2, 40]
    - `target`: int sum that want a combination of `candidates` to add up to
  - output: int array of all possible unique int subarray combinations that each sum up to `target`
    - empty if there is no valid combination
    - each combination can reuse the same int el from `candidates` any number of times
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(N ^ T)? T & and O(N ^ T)? S solution
- initialise empty res array
- helper recursive function `backtrack(comb, currSum startPos)`
  - if i is out of bounds or currSum < target, return
  - if currSum == target, push copy of comb to res and return
  - push candidates\[i] to comb
  - backtrack(comb, currSum - candidates\[i], startPos) 
    - includes candidates\[i] from all branching out combos
  - pop from comb
  - backtrack(comb, currSum, startPos + 1)
    - excludes candidates\[i] from all branching out combos
  - no loop to iterate thru all els in `candidates` to avoid duplicates
- backtrack([], target, i)
- return res