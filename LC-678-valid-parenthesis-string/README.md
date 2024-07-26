# [LC 678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)

## General Notes

- PEDAC: Problem
  - input:
    - `s`: a string
      - whose characters are `(`, `)`, or `*` only
      - of size in the range \[1, 100]
  - output:
    - `res`: a bool that is true if `s` is a valid string else false
  - `s` is a valid string IFF:
    - all `(`'s must be closed by a following `)`
    - all `)`'s must be opened by a preceeding `(`
    - `*` is an `""` (empty string), a `(`, or a `)`
- PEDAC: Examples
  - a valid `s` cannot start with a `)`
  - a valid `s` may have any number of `*`'s

## Solution 1: greedy (NeetCode's modded)

- O(N) T and O(1) S solution
- initialise variables
  - `leftMin`: int set to 0 that tracks the min possible left parentheses existing in `s` at some time
  - `leftMax`: in set to 0 that tracks the max possible left parenthess existing in `s` at some time
- loop thru each char `c` in `s`,
  - if `c` is a `(`
    - `leftMin++`
    - `leftMax++`
  - else if `c` is a `)`
    - `leftMin` = max of (`leftMin` - 1, 0)
      - reset to 0 if it goes negative
    - `leftMax--`
  - else
    - `c` is a `*`
    - `leftMin` = max of (`leftMin` - 1, 0)
    - `leftMax++`
  - if `leftMax` < 0,
    - means not enough left parentheses to open right parentheses
    - return false
- return `leftMin` == 0
  - `leftMin`'s min value is 0 because of resetting
  - if `leftMin` > 0,
    - means not enought right parentheses to close left parentheses
