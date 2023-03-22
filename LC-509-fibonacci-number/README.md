# [LC 509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

## General Notes

- PEDAC: Problem
  - input: int n in range \[0, 30]
  - ouput: int res of F(n)
  - F(0) = 0, F(1) = 1
  - F(n) = F(n - 1) + F(n - 2)
- PEDAC: Examples

## Solution 1: recursive with memoization (top-down DP)

- O(N) time and O(N) space solution
- initialise memo hash table or array with values \[1, 1]
- helper recursive function recurse(n)
  - if n is 0 or 1, return n
  - if n in memo, return memo\[n]
  - get result of and store it in memo\[n] = recurse(n - 1) + recurse(n - 2)
  - return memo\[n]

## Solution 2: iterative with memoization (bot-up DP)

- O(N) time and O(N) space solution
- similar approach as solution 1 recursive with memo but
  - use while loop to build up result of F(N) until reaching N
  - still use memo array / hash table

## Solution 3: iterative with memoization (bot-up DP)

- O(N) time and O(1) space solution
- similar approach as solution 2 iterative with memo but
  - replace memo array / hash table with pointers to last 2 F(n) terms (ints)