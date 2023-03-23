# [LC 70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

## General Notes

- PEDAC: Problem
  - input: int n in range \[1, 45]
  - ouput: int res of F(n)
  - count distinct ways to climb to top
  - each time can climb either 1 or 2 steps
  - same recurrence relation as fibonacci but base cases start at n = 1, n = 2
  - F(1) = 1, F(2) = 2
  - F(n) = F(n - 1) + F(n - 2)
- PEDAC: Examples
  - F(0) = undefined
  - F(1) = 1
  - F(2) = 2
  - F(3) = 3
  - F(4) = F(2) + F(3) = 5

## Solution 1: recursive with memoization (top-down DP)

- O(N) time and O(N) space solution
- initialise memo hash table or array with values \[1, 1]
- helper recursive function recurse(n)
  - if n is 1 or 2, return n
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