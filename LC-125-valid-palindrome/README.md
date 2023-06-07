# [LC 125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

## General Notes

- PEDAC: Problem
  - input:
    - `s`: string containing ASCII chars
      - of size in range \[1, 2 * 10^5]
  - output:
    - `res`: boolean indicating if `s` is a palindrome or not
  - ignore non-alphanumeric chars
  - treat `s` case-insensitively
    - e.g. consider `a` the same as `A`
- PEDAC: Examples

## Solution 1: two pointers

- O(N) T and O(N) S solution
- helper function isAlphaNum(c)
  - returns true if `c` is a numerical digit or alphabet char else return false
- initialise variables
  - `l`: int set to 0 that represents the left pointer of `s` starting from its first character
  - `r`: int set to size of `s` -1 that represents the right pointer of `s` starting from its last char
- while `l` <= `r`
  - while `s[l]` is not an alphanumeric char and `l` < `r`
    - `l++`
  - while `s[r]` is not an alphanumeric char and `r` > `l`
    - `r--`
  - if lowercased `s[l]` != lowercased `s[r]`, return false
  - `l++`
  - `r--`
- return true if exited loop
