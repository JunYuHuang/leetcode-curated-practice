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

## Solution 2: stack optimized (StefanPochmann's modified)

- O(1) (amoritized) time and O(N) space class solution
- since each element only gets moved from input to output stack once and only after spent time pushing it,
  amoritized time for each operation is O(1)
- had slower runtime on LC submission vs solution 1 (beats 30.69% vs 70.54%) 🤔
- class has 2 arrays inputStack and outputStack
- push elements to inputStack
- peek() moves all elements from inputStack to outputStack
- pop() calls peek() and pops from outputStack
- empty() is same as in solution 1
