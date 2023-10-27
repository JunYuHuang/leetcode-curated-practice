# [LC 42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)

## General Notes

- PEDAC: Problem
  - inputs
    - `height`: int array that represents an elevation map where each element `height[i]` is a block of height `height[i]` and of width 1
      - of size in range \[1, 2 * 10^4]
      - of values in range \[0, 10^5]
  - output
    - `res`: non-negative int that represents the max rainwater units the elevation map can trap after raining
  - constraints
    - rainwater trapped must be between 2+ blocks or "pillars" of elevation that have at least 1 block that is lower than the heights of both starting and ending pillars

## Solution 1: two pointers (NeetCode's modded)

- O(N) T and O(1) S solution
- return 0 if size of `height` is < 3 because cannot store water at endpoints (first and last element / bar)
- initialise variables `l`, `r`, `maxL`, `maxR`, `res`
  - `l`: pointer / index for 1st el in `height` set to 0
  - `r`: pointer / index for last el in `height` set to size of `height` - 1
  - `maxL`: largest value that `height[l]` has encountered so far
  - `maxR`: largest value that `height[r]` has encountered so far
- iterate thru `height` while `l` < `r`
  - move the pointer associated with the lesser `max`-prefixed value, else move the other pointer
    - i.e. `l++` if `maxL` < `maxR` else `r--`
  - process the element represented by the pointer that was moved
  - only add the calculated water stored `water` to `res` if `water` > 0
  - update `maxL` if `l` was moved and encountered a greater element
  - update `maxR` ir `r` was moved and encountered a greater element
  - `water` calculation
    - = `maxL` - `height[l]` if `maxL` was < `maxR`
    - = `maxR` - `height[r]` if `maxL` was >= `maxR`
  - return `res`
