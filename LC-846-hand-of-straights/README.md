# [LC 846. Hand of Straights](https://leetcode.com/problems/hand-of-straights/)

## General Notes

- PEDAC: Problem
  - input:
    - `hand`: non-empty int array
      - of size `n` in the range \[1, 10^4]
      - of values in the range \[0, 10^9]
    - `groupSize`: int in the range \[1, `n`]
  - output:
    - `res`: bool
- PEDAC: Examples
  - length of `hand` is not divisible by `groupSize` -> false

## Solution 1: greedy

- O(NLogN) T and O(N) S solution
- if `hand.length` % `groupSize` != 0,
  - return false
- initialise variables
  - `count`: hashmap that maps each unique int to its occurrences in `hand`
- sort `hand` in ASC order
- for `card` in `hand`,
  - if `count[card]` == 0,
    - continue
  - for `i` from 0 to `groupSize` - 1 inclusive,
    - `nextCard` = `card` + `i`
    - if `nextCard` is not in `count`,
      - return false
    - if `count[nextCard]` == 0,
      - return false
    - `count[nextCard]--`
    - if `count[nextCard]` < 0,
      - return false
- return true
