# [LC 20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## General Notes

- PEDAC: Problem
  - input:
    - `s`: string of
      - of size in range \[1, 10^4]
      - of parentheses chars only in set `()[]{}`
  - output:
    - `res`: bool that indicates if `s` has valid parentheses or not
  - `s` is valid IFF:
    - open brackets must be closed by same associated closing brackets
    - open brackets must be closed in correct order
    - every close bracket has associated open bracket of same type
- PEDAC: Examples
  - false if `s` starts with an open parentheses `([{`
  - false if number of open parentheses of a type is different (i.e. > or < and not ==) from the number of closed parentheses of the same type
  - false if open parentheses of a type is closed by a different type of closed parentheses
  - false if `s` is odd-lengthed

## Solution 1: stack (NeetCode's modded)

- O(N) T and O(N) S solution
- initialise variables
  - `stack`: array stack for storing closed parentheses
  - `closeToOpen`: hashmap that maps each type of closing parentheses char to its associated open parentheses of the same type (3 key-value pairs)
- optional: return false if `s`'s first char is a closed parentheses or length of `s` is odd
- loop thru every char `c` in `s`
  - if `c` is a closing parentheses char,
    - if `stack` is not empty and `stack`'s last element (an open parentheses char) is the same as `c`'s associated open parenthese char
      - pop from `stack`
    - else return False
  - else `c` is an open parentheses char,
    - push `c` to `stack`
- return true if `stack` is empty else false
