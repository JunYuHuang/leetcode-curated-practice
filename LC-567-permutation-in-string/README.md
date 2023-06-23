# [LC 567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

## General Notes

- PEDAC: Problem
  - input:
    - `s1`: string of only lowercase English letters
      - of size in range \[1, 10^4]
    - `s2`: string of only lowercase English letters
      - of size in range \[1, 10^4]
  - output:
    - `res`: boolean that indicates if `s2` contains a permutation of `s1`
  - permutation = any arrangement of all the characters in a string
  - `s2` contains a permutation of `s1` IFF:
    - `s2`'s size >= `s1`'s size
    - the perm. substring in `s2`:
      - has size == size of `s1`
      - has the same set of unique chars as in `s1`
      - has the same count of the same set of unique chars as in `s1`
- PEDAC: Examples

## Solution 1: sliding window

- O(26 * N) T and O(1) S solution
- initialise variables
  - `s1Len`: size of `s1`
  - `s2Len`: size of `s2`
  - `s3`: `s1` appended with `s2`
  - `s1Count`: hashmap that maps each unique char in `s1` to its # of occurrences initialised with unique keys from `s3`
  - `s2Count`: hashmap that maps each unique char in `s2` to its # of occurrences initialised with unique keys from `s3`
  - `l`: left pointer for `s2` set to 0
  - `r`: right pointer for `s2` set to 0
- loop thru `s1` and build `s1Count` hashmap
- while `r` < `s2Len`:
  - `s2Count[s2[r]]++`
  - `windowSize` = `r` -`l` + 1
  - if `windowSize` == `s1Len`
    - if `s2Count` == `s1Count`
      - return true
    - `s2Count[s1[l]]--`
    - `l++`
  - `r++`
- return false
