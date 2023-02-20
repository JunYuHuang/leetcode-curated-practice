# [LC 200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

## Solution 1: DFS recursive

- O(M \* N) time and O(M \* N) space solution
- initialise visit set, res int to 0
- helper recursive function dfs(r, c):
  - if (r, c) is out of bounds or visited or a "0": return
  - visit (r, c)
  - for each of (r, c)'s 4 adjacent vert. and horiz. neighbors
    - run recursive call on them
- loop thru matrix
  - if (r, c) not visited and is a "1"
    - dfs(r, c)
    - res++
- return res
