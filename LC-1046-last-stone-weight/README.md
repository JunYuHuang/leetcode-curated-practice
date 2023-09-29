# [LC 1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `stones`: int array that represents stones of varying weights where `stones[i]` is the weight of the `i`th stone
      - of size in the range \[1, 30]
      - of values in the range \[1, 1000]
  - output:
    - `res`: int that represents the weight of the last remaining stone or 0 if there are no stones left
      - of a value in the range \[0, 1000]
  - stone game loop
    - continue while there are 2+ stones left
- PEDAC: Examples

## Solution 1: max heap

- O(NLogN) T and O(N) S solution
- initialise variables
  - `maxHeap`: max heap initialised with `stones` array
- while `maxHeap` has 2+ elements
  - `stoneX` = pop from `maxHeap`
  - `stoneY` = pop from `maxHeap`
  - if `stoneX` == `stoneY`, continue
  - `newStone` = `abs(stoneX - stoneY)`
  - push `newStone` to `maxHeap`
- return `maxHeap[0]` if `maxHeap` is non-empty else 0
