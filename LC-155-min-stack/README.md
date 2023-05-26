# [LC 155. Min Stack](https://leetcode.com/problems/min-stack/)

## General Notes

- PEDAC: Problem
  - `stack` class methods and their I/O
    - `stack()`: constructor
    - `push(val)`: pushes an int `val` to the stack
    - `pop()`: removes the element on top of stack
    - `top()`: gets the top element of the stack
    - `getMin()`: gets min element in stack
  - constraints
    - `val` is value in range \[-2^31, 2^31 - 1]
    - `pop`, `top`, `getMin` will be called on non-empty stacks
    - all methods must have O(1) time complexity
- PEDAC: Examples

## Solution 1: 2 stacks (NeetCode's modded)

- O(N) T and O(N) S solution
- `stack()` constructor initialises variables
  - `stack`: empty array that is also stack
    - store subarrays of size of (element, minElementNow)
- `push(val)`:
  - if `stack` is empty,
    - push `[val, val]` to `stack` and return
  - else
    - `lastMin` = `stack[-1][1]`
    - push `[val, min(val, lastMin)]` to `stack`
- `pop()`:
  - pops from `stack`
- `top()`:
  - return `stack[-1][0]`
- `getMin()`
  - returns `stack[-1][1]`
