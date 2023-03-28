# [LC 779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/)

## General Notes

- PEDAC: Problem
  - input: 
    - `n`: int in range \[1, 30]
    - `k`: int in range \[1, 2^n - 1]
  - output: int that is either 0 or 1
  - table of 1-indexed `n` rows
  - both `n` and `k` are 1-indexed
  - `n` = row index from 1
  - `k` = col index from 1
  - what is recurrence relation?

  - resembles perfect binary trees of nodes 1s and 0s
- PEDAC: Examples
  - n = 1, k = 1
    - row

## Solution 1: iterative BFS brute force (TLE)

- O(2^N) time and O(2^N) space solution
- use nested loop to generate the "nodes" in each "level" or row and store them in a levels array
- return level\[k - 1]

## Solution 2: recursive (repititionismastery's modded)

- O(LogK) time and O(N) space solution
- does reverse DFS on "binary tree"?
- patterns
  - parent of `kth` index in `nth` row is
    - `k/2` index in `n-1` row for even numbered indices
    - `(k+1)/2` index in `n-1` row for odd numbered indices
  - `kth` value of index in `nth` row is
    - flipped / reversed value of parent in `n-1` row for even numbered indices
    - same value as parent in `n-1` row for odd numbered indices
- make function recursive
  - if N is 1, return 0
  - get parent = recursive call on (N - 1, (k + 1) / 2)
  - if K is even
    - return opposite of parent
  - else
    - return parent
