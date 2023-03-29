# [LC 912. Sort an Array](https://leetcode.com/problems/sort-an-array/)

## General Notes

- PEDAC: Problem
  - input: 
    - `nums`: int array in range \[1, 5 * 10^4]
  - output: 
    - `nums` but sorted in ascending order
- PEDAC: Examples

## Solution 1: merge sort D&C recursive bot-up (NeetCode)

- O(NLogN) T and O(N) S solution
- in-place merge sort algorithm
- define helper functions
  - recursive mergeSort(arr, l, r)
  - merge(arr, L, M, R)
- mergeSort(arr, l, r)
  - if l == r, return arr
  - m (pivot) = (l + r) // 2
  - mergeSort(arr, l, m) to sort left sublist
  - mergeSort(arr, m + 1, r) to sort right sublist
  - merge(arr, l, m, r)
  - return arr
- merge(arr, L, M, R)
  - create left and right sublists from L, M, R
    - left includes arr\[M]
  - traverse both left and right sublists and sort them in arr in-place
  - for remaining elements in left or right, assign them to nums array
- return mergeSort(nums, 0, len(nums) - 1)