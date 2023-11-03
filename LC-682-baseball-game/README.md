# [LC 682. Baseball Game](https://leetcode.com/problems/baseball-game/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `operations`: string array where each element represents an operation to apply
      - of size in range \[1, 1000]
      - of values in the set { `C`, `D`, `+`, or string that represents an integer in the range [-3 * 10^4, 3 * 10^4] }
  - output:
    - `res`: int representing the sum of all scores on the record after applying all the operations
  - constraints
    - all `+`, `C`, and `D` operations will always be valid
- PEDAC: Examples

## Solution 1: stack

- O(N) T and O(N) S solution
- initialise variables
  - `records`: int array that is initially empty
- loop for each element `o` in `operations`
  - if `o` is a `'+'` char,
    - push `records[-1]` + `records[-2]` to `records`
  - else if `o` is a `'D'` char,
    - push `records[-1]` * 2 to `records`
  - else if `o` is a `C` char,
    - pop the last int from `records`
  - else (`o` is an int char)
    - push `o` cast as an int to `records`
- return sum of all ints in `records`
