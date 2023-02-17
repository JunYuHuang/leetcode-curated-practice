# [LC 394. Decode String](https://leetcode.com/problems/decode-string/)

## Solution 1: stack (NeetCode's modified)

- O(maxK \* countK \* N) time and O(maxK \* countK \* N) space stack solution
- pop and process innermost nested brackets before outside brackets
- stack array to store all non-`]` chars
- only process chars in stack once `]` encountered
- for pos, char in str
  - if char is not `]`, push it to stack and continue to next loop / iteration
  - initialise empty temp stack array
  - while stack is not empty and stack top is not a digit
    - curr = pop from stack
    - if curr is not `[`, push it to temp
  - initialise times int to 0 and i int to 0
  - while stack is not empty and stack top is a digit
    - curr = pop from stack
    - times = times + int(curr) \* (10^i)
    - i++
  - res = times \* temp reversed converted to a string
  - push res to stack
- return stack as string
