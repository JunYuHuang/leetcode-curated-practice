# [LC 93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

## General Notes

- PEDAC: Problem
  - input: 
    - `s`: string of only numerical digits and of size in the range \[1, 20]
      - valid size range: \[4, 12]
  - output: 
    - string array of all possible IPv4 strings derived from `s`
      - empty if there are no valid addresses
  - valid IPv4 address IFF:
    - has 3 dots that separate 4 integers (octets)
    - of size in range \[7, 15]
  - valid IPv4 address integer / octet:
    - in the range \[0, 255]
      - parse as int and check
    - has no leading zeroes
      - 1st char can only be 0 if octet is of size 1
      - ok: 0
      - no: 01, 00
    - of size in range \[1, 3]
- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's modded)

- O(3^4 * 4) T and O(3 * 4) S solution
- if `s`'s size is not in range \[4, 12], return []
- initialise empty `res` array
- helper function `isOctet(l, r)`
  - if 1st char of `s\[l:r + 1]` is 0 and its size !== 1, return false
  - return true if `s\[l:r + 1]` as an int is in the range \[0, 255] else false
- recursive helper `backtrack(curr, size, l)`:
  - if `l` is out of bounds
    - if `curr` is of size 4 and `size` == len(s)
      - push copy of `curr` as a string joined with `.` to `res`
    - return
  - loop for `r` in range \[l, min(l + 3, len(s))]:
    - if `s[l:r + 1]` is a valid octet
      - push `s[l:r + 1]` to `curr`
      - `backtrack(curr, r + 1)`
      - pop from `curr`
- `backtrack([], 0)`
- return `res`