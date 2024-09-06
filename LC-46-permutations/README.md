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

## Solution 1: recursive backtracking 1 (mine)

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

## Solution 2: recursive backtracking 2 (mine)

- O(N \* !N) T and O(N \* !N) S solution
- initialise variables
  - `res`: set to empty array
  - `N`: set to length of `nums`
- define function `dfs(perm, used)`
  - if `perm`'s length >= `N`,
    - push copy of `perm` to `res`
    - return
  - loop thru every element `n` in `nums`,
    - if `n` is in `used`,
      - continue
    - push `n` to `perm`
    - add `n` to `used`
    - `dfs(perm, used)`
    - pop from `perm`
    - remove `n` from `used`
- `dfs([], empty set)`
- return `res`

## Solution 3: recursive backtracking 3 (NeetCode's modded)

- O(N^2 \* !N) T and O(N^2 \* !N) S solution
- if `nums` is empty,
  - return `[[]]`
- set `res` to empty array
- set `perms` to `permute(nums[1:])`
- loop thru every subarray `perm` in `perms`,
  - loop thru `i` from 0 to `perm`'s length inclusive,
    - set `perm_copy` to copy of `perm`
    - insert `nums[0]` before index `i` of `perm_copy`
    - push `perm_copy` to `res`
- return `res`

## Solution 4: iterative backtracking (NeetCode's modded)

- O(N^2 \* !N) T and O(!N) S solution
- same approach as solution 3 but
  - swap recursive call with outer loop for iterating thru `nums`
  - reassign `perms` to new `perms` before iterating next number in outer loop
