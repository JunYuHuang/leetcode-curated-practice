# [LC 242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## General Notes

- PEDAC: Problem
  - input:
    - `s`, `t`: strings of size in range \[1, 5 * 10^4] of lowercase English letters and of the same length
  - output:
    - boolean that indicates if `t` is an anagram of `s`
- PEDAC: Examples

## Solution 1: hashmap brute force

- O(N) time and O(N) space solution
- return false if `t` and `s` are of different lengths
- initialise empty hashmap `charToCount`
- loop thru each char in `s` to build `charToCount`
- loop thru each char `c` in `t`
  - if `c` is not in `charToCount`, return false
  - `charToCount[c]--`
  - if `charToCount[c]` < 0, return false
- loop thru each value in `charToCount`
  - if value is not 0, return false
- return true
