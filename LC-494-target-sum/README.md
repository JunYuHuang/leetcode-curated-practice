# [LC 494. Target Sum](https://leetcode.com/problems/target-sum/)

## Solution 1: DFS recursive brute force (TLE)

- O(2^N) time and O(2^N) space solution
- res int initialised to 0
- helper recursive function dfs(curr, i)
  - if i == last position + 1 (out of bounds)
    - if curr == target, res ++
    - return
  - call itself recursively on (curr + nums\[i], i + 1)
  - call itself recursively on (curr - nums\[i], i + 1)
- dfs(0, 0)
- return res

## Solution 2: top-down / recursive DP (NeetCode's modified)

- O(NT) time and O(NT) space solution where T = sum(nums)
- same approach as solution 1 but
  - with memoization
  - no res int variable
  - helper recursive function dfs()
    - returns the # of ways to reach to target
    - is a pure function
  - directly return result of calling dfs(0, 0)
- memo dictionary that maps (curr, i) -> # of ways to get to target from (curr, i)
- helper recursive function dfs(curr, i)
  - base case = if i reaches the last position of the input array + 1 (out of bounds)
    - return 1 if curr equals target else 0
  - return cached result if (curr, i) is there
  - add = recursive call adding nums\[i] to curr and i++
  - minus = recursive call subtracting nums\[i] from curr and i++
  - cache result sum of add and minus for (curr, i)
  - return memo of (curr, i)
- return dfs(0, 0)
