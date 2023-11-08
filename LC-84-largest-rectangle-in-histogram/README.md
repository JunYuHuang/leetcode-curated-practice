# [LC 84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## General Notes

- PEDAC: Problem
  - input:
    - `heights`: int array where each element represents a bar height
      - of size in range \[1, 10^5]
      - of values in range \[0, 10^4]
      - each element / bar has a width of 1
  - output:
    - `res`: int representing the largest rectangle (by area) in the histogram
      - of value in range \[0, 10^8]
  - find the rectangle with the max area
  - cannot sort `heights`
  - rectangles
    - area of 1 bar = 1 x `heights[i]`
    - area of 2+ bars = (# of bars) x min(heights of bars)
- PEDAC: Examples

## Solution 1: monotonic increasing stack (NeetCode's modded)

- O(N) T and O(N) S solution
- summary
  - build and maintain monotonic increasing stack of `(i, heights[i])` elements by looping through `heights`
  - store area of largest rectangle in int variable `res`
  - only update `res` when:
    - current `heights[i]` > height in top of stack so need to pop elements from stack to maintain its monotonic increasing property
    - potentionally update `res` if popped element's area is greater than it
  - calculate area for an element `el` in `heights`
    - = (`i` - `el[0]`) * `el[1]` when looping thru `heights` the first time
    - = (size of `heights` - `el[0]`) * `el[1]` when popping any remaining elements from the stack after finished looping thru `heights` once
  - pushing elements to the stack
    - if didn't need to pop any elements from the stack,
      - push (`i`, `heights[i]`) to the stack
    - else if needed to pop any elements from the stack,
      - push (`i` of last popped element, `heights[i]`) to the stack
