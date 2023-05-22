# [LC 128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in range \[0, 10^5]
      - of values in range \[-10^9, 10^9]
      - unsorted
  - output:
    - `res`: int that is the length of the longest consecutive elements sequence
  - constraints
    - must write O(N) time algorithm (e.g. cannot sort array)
- PEDAC: Examples

## Solution 1: set solution (NeetCode's modded / expl.)

- O(N) T and O(N) S solution
- initialise variables
  - `res`: int initially set to 0
  - `numsSet`: set created from `nums`
- loop thru each el `n` in `nums`
  - if `n` has a left adjacent neighbour (`n-1` exists),
    - continue
  - if not continued, we know `n` is the start of a sequence
  - `count` = 1
  - while `n + count` exists,
    - `count`++
  - if `count` > `res`, update `res` to equal `count`
- return `res`
