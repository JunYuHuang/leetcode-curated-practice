# [LC 40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

## General Notes

- PEDAC: Problem
  - input: 
    - `candidates`: int array of size in range \[1, 100] and of values in range \[1, 50]
      - may have duplicate values
    - `target`: int of value in range \[1, 30]
  - output:
    - array of int subarrays that represent all unique combos whose ints sum up to `target`
      - each subarray uses each int from `candidate` only once
      - no duplicate subarrays (order doesn't matter)
    - of size in range \[1, N]
  - backtrack(curr, i) helper function
    - return if i is out of bounds or sum(curr) > target
    - keep adding elements if sum(curr) < target
    - found solution if i is in bounds and sum(curr) == target
    - how to guarantee solutions in res array are unique combinations?
      - sort input array `candidates` and when excluding an el skip to next diff el
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's expl.)

- O(2^N)? T & and O(2^N)? S solution
- sort input array `candidates`
- initialise empty res array
- helper recursive function `backtrack(comb, i, currSum)`
  - if `currSum` equals target, push copy of `comb` to res and return
  - if `i` is out of bounds or `currSum` > target, return
  - push `candidates[i]` to comb
  - `backtrack(comb, i + 1, currSum - candidates[i])`
  - pop from `comb`
  - keep incrementing `i` while `i + 1` is in bounds and `candidates[i]` is the same as `candidates[i + 1]`
  - `backtrack(comb, i + 1, currSum)`
- call `backtrack([], 0, currSum)` and return res
- **Important: must write good base case (currSum == target) before bad base cases (i out of bounds or currSum > target) in recursive function**
