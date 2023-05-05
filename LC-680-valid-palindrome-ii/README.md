# [LC 680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)

## General Notes

- PEDAC: Problem
  - input:
    - `s`: string of size in range `[1, 10^5]`
  - output: boolean that indicates if `s` can be a palindrome after deleting at most on character from `s`
  -
- PEDAC: Examples

## Solution 1: brute force (TLE)

- O(N^2) T and O(1) S solution
- helper function `isPalindrome(string)`
  - returns true if `string` is a palindrome else false
- if `isPalindrome(s)`, return true
- loop for `i` in range \[0, len(s) - 1]
  - if `isPalindrome(s[:i] + s[i + 1:])` returns true, return true
- return false if exited loop

## Solution 2: two pointers (NeetCode)

- O(N) T and O(1) S solution
- helper function `isPalindrome(string)` that returns true or false
- initialise variables
  - `l`: int set to 0
  - `r`: int set to len(s) - 1
- repeat same logic as `isPalindrome(string)` but
  - for checking if `string[l]` == `string[r]`,
    - return result of `skipL` OR'd with `skipR`
    - `skipL`: substring of string excluding the char at the `l` pointer
    - `skipR`: substring of string excluding the char at the `r` pointer
