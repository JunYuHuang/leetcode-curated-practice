# [LC 3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## General Notes

- PEDAC: Problem
  - input:
    - `s`: string of size in range \[0, 5 * 10^4]
      - of English alphabetical chars, numerical digits, symbols and spces
  - output:
    - `res`: int that represents the length of the longest unbroken substring in `s` with no repeating characters
      - int in range \[0, 5 * 10^4]
  - notes
    - return size of `s` if its size is <= 1
- PEDAC: Examples

## Solution 1: sliding window (NeetCode's expl.)

- O(N) T and O(N) S solution
- initialise variables
  - `res`: int set to 0
  - `l`: left pointer for `s` set to 0
  - `r`: right pointer for `s` set to 0
  - `seen`: empty single-char string set
  - `N`: length of `s`
- return `N` if `N` <= 1
- while `r` < `N`
  - while `l` < `r` and `s[r]` is in `seen`
    - remove `s[l]` from `seen`
    - `l++`
  - add `s[r]` to `seen`
  - `windowSize` = `r` - `l` + 1
  - update `res` to `windowSize` if `windowSize` > `res`
  - `r++`
- return `res`
