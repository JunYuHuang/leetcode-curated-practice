# [LC 278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

## General Notes

- PEDAC: Problem
  - input:
    - `n`: int in range \[1, 2^31 - 1]
  - output:
    - `pick`: int in range \[1, `n`]
  - constraints
    - guaranteed to have at least 1 bad version
- PEDAC: Examples

## Solution 1: binary search

- O(LogN) T and O(1) S solution
- modified binary search
  - `l`: int (pointer) set to 1
  - `r`: int (pointer) set to `n`
  - `m`: int mid pointer
  - `mRes`: `isBadVersion(m)`
  - if `n` is 1, return 1
  - if `mRes` is true and `isBadVersion(m - 1)` is false,
    - return `m`
  - else if `mRes` is true,
    - search left half (`r` = `m` - 1)
  - else (if `mRes` is false)
    - search right half (`l` = `m` + 1)
