# [LC 374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

## General Notes

- PEDAC: Problem
  - input:
    - `n`: int in range \[1, 2^31 - 1]
  - output:
    - `pick`: int in range \[1, `n`]
- PEDAC: Examples

## Solution 1: binary search

- O(LogN) T and O(1) S solution
- initialise variables
  - `l`: int (pointer) set to 0
  - `r`: int (pointer) set to `n`
- while true
  - `m` = `l` + (`r` - `l`) / 2 rounded down to nearest int
  - `guessRes` = `guess(m)`
  - if `guess(m)` is 0,
    - return `m`
  - else if `guess(m)` is -1 (`m` > `pick`),
    - `r` = `m` - 1
  - else if `guess(m)` is 1 (`m` < `pick`),
    - `l` = `m` + 1
