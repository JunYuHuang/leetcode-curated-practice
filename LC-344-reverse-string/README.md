# [LC 344. Reverse String](https://leetcode.com/problems/reverse-string/)

## General Notes

- PEDAC: Problem
  - input: array of string characters of length 1+
  - ouput: none; modify array in-place
- PEDAC: Examples

## Solution 1: iterative

- O(N) time and O(1) space solution
- initialise pointers L & R pointing to start and end of array
- while L <= R
  - if L & R point to different characters, swap them
  - L++
  - R--

## Solution 2: recursive

- O(N) time and O(N) space solution
- same approach as solution 1 iterative but
  - replace while loop with recursive helper function calls