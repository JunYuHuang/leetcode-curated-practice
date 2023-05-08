# [LC 217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array of size in range \[1, 10^5] with values in range \[-10^9, 10^9]
  - output:
    - boolean that indicates if there is a value in `nums` that appears 2 times or more
- PEDAC: Examples

## Solution 1: hashmap

- O(N) time and O(N) space solution
- initialise empty hashmap `count`
- loop thru each int `n` in `nums`
  - if `n` is in hashmap, increment its value by 1
  - else add `n` as a new pair (`n`, 1) to the hashmap
  - if `count[n]` >= 2, return true
- return false if exited loop

## Solution 2: set (NeetCode's modded)

- O(N) time and O(N) space solution
- initialise empty set `visit`
- loop thru each int `n` in `nums`
  - if `n` is in `visit`, return true
  - add `n` to `visit`
- return false if exited loop
