# [LC 11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

## General Notes

- PEDAC: Problem
  - input:
    - `height`: unsorted int array that represents vertical lines of a container
      - of size in range \[2, 10^5]
      - of values in range \[0, 10^4]
  - output:
    - `res`: int that represents that max area of water that a container defined by 2 distinct line elements from `height` can hold
      - in range \[0, max(`height`) * size of `height`]
  - constraints
    - cannot slant container at an angle
    - cannot sort `height`
  - area between any 2 vertical lines `height[i]` and `height[j]` = min(`height[i]`, `height[j]`) * (`j` - `i`) where
    - 0 <= `i` < `j` < size of `height`
    - `i` != `j`
- PEDAC: Examples

## Solution 1: two pointers

- O(N) T and O(1) S two pointers solution
- initialise variables
  - `res`: int set to 0
  - `l`: int set to 0 that represents the left pointer in `height`
  - `r`: int set to size of `height` - 1 that represents the right pointer in `height`
- while `l` < `r`:
  - calculate the area given the current pointers
    - `area` = min(`height[l]`, `height[r]`) * (`r` - `l`)
  - update `res` to `area` if `area` > `res`
  - move the pointer that decreases the next window (formed by `height[l:r+1])'s min height value the least
    - if `height[l]` < `height[r]`, `l++`
    - else if `height[l]` > `height[r]`, `r--`
    - else (`height[l]` == `height[r]`),
      - doesn't matter which one we move??
      - either `l++` or `r--`
- return `res`
