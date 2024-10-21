# [LC 1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `stones`: int array that represents stones of varying weights
      - `stones[i]` is the weight of the `i`th stone
      - of size in the range \[1, 30]
      - of values in the range \[1, 1000]
  - output:
    - `res`: int that represents the weight of the last remaining stone or 0 if there are no stones left
      - of a value in the range \[0, 1000]
  - stone game loop
    - continue while there are 2+ stones left
- PEDAC: Examples

## Solution 1: max heap (NeetCode's modded)

- O(NLogN) T and O(N) S solution
- make `stones` into a max heap
- while `stones`'s length is greater than 1,
  - set `stoneX` to heap popped int from `stones`
  - set `stoneY` to heap popped int from `stones`
  - if `stoneX` equals `stoneY`,
    - continue
  - set `newStone` to absolute value of result of `stoneX` - `stoneY`
  - heap push `newStone` to `stones`
- if `stones` is empty,
  - return 0
- else,
  - return top / root of `stones`
