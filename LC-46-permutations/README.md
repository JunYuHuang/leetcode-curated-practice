# [LC 46. Permutations](https://leetcode.com/problems/permutations/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: non-empty int array
      - of size in range \[1, 6]
      - of values in range \[-10, 10]
      - of all unique values
  - output:
    - `res`: array of int arrays
      - each subarray is a permutation of `nums`
      - should not have duplicate subarrays
  - `perm` is a permutation of `nums` IFF
    - they are of equal length
    - they have the same elements
    - `perm` has the elements in `nums` in some order
      - order may be the same or different as `nums`
    - each reordering of `nums`' elements is a permutation
- PEDAC: Examples

## Solution 1: recursive backtracking (mine)

- O(N \* !N) T and O(N \* !N) S solution
- initialise variables
  - `res`: set to empty array
  - `N`: set to length of `nums`
- define function `dfs(perm, cur_nums)`
  - if `perm`'s length >= `N`,
    - push copy of `perm` to `res`
    - return
  - loop thru every index `i` in `cur_nums`,
    - push `cur_nums[i]` to `perm`
    - `new_nums` = copy of `cur_nums` excluding element at index `i`
    - `dfs(perm, new_nums)`
    - pop from `perm`
- `dfs([], nums)`
- return `res`
