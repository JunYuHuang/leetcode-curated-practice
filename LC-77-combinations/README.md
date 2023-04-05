# [LC 77. Combinations](https://leetcode.com/problems/combinations/)

## General Notes

- PEDAC: Problem
  - input: 
    - `n`: int in range \[1, 20]
    - `k`: int in range \[1, `n`]
  - output: 
    - matrix; array of int arrays
  - `n` is the inclusive upper bound of the range of numbers
  - `k` is the length of each int subarray or set in the results array
- PEDAC: Examples

## Solution 1: DFS backtracking (NeetCode's)

- O(K * N^K) T and O(K * N^K) S solution
- initialise global empty res array
- recursive helper function `backtrack(startPos, combArr)`
  - base case: if array `combArr` has reached length `k`, 
    - add a copy of it to `res` array
  - loop thru ints in range \[`startPos`, `n`]
    - push current int to `combArr`
    - call itself recursively on (i + 1, combArr)
    - pop current int from `combArr`
- call `backtrack(1, [])` and return res
