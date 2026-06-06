# [LC 14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## General Notes

- PEDAC: Problem
  - input:
    - `strs`: string array
      - of size in range \[1, 200]
      - of elements `strs[i]` where:
        - length in range \[0, 200]
        - of only lowercase English letter chars
  - output:
    - `res`: string
      - length in range \[0, 200]
      - of only lowercase English letter chars
      - longest prefix substring shared by all string elements in `strs`
- PEDAC: Examples
  - TODO

## Solution 1: NeetCode's iterative array modded solution

- O(m * n) T and O(n) S solution
- if `strs` is of size 1,
  - return `strs[0]`
- set int `firstLen` to size of `strs[0]`
- set int `strsLen` to size of `strs`
- set string array `res` empty
- loop for int index `i` from 0 to (`strsLen` - 1) inclusive:
  - loop for int index `j` from 1 to (`firstLen` - 1) inclusive:
    - if `i` >= length of `strs[j]` or `strs[j][i]` != `strs[0][i]`:
      - return `res` as a converted by joining all elements with an empty space char
  - push `strs[0][i]` to `res`
- return `res` as a converted by joining all elements with an empty space char
