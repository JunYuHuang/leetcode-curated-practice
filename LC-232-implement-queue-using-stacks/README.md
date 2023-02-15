# [LC 232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

## Solution 1: stack w/ brute force

- O(N) time and O(N) space class solution
- class has 2 arrays stack and reverseStack
- always keep all elements in only 1 of the stacks at any time based on the method needed
- helper function moveStk(src, dst) -> for el in src, pop it and push it to dst stack / array
- push(x) -> moveStk(revStk, stk), push x to stk
- pop() -> moveStk(stk, revStk), pop from revStk
- peek() -> moveStk(stk, revStk), ret revStk\[-1]
- empty() -> ret !stk & !revStk
