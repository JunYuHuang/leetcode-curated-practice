# [LC 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## General Notes

- PEDAC: Problem
  - input:
    - `list1`: head `ListNode` of list that may be null
      - of size in range \[0, 50]
      - of nodes whose values are in range \[-100, 100]
    - `list2`: head `ListNode` of list that may be null
      - of size in range \[0, 50]
      - of nodes whose values are in range \[-100, 100]
  - output:
    - `res`: head `ListNode`` of sorted merged list
      - of size in range \[0, 100]
      - of nodes whose values are in range \[-100, 100]
      - should be sorted in non-decreasing order
  - both `list1` and `list2` are sorted in non-decreasing order

- PEDAC: Examples
  - null `list1`, `list2` = \[0, 1, 2]
    - res = `list2`
  - both `list1` and `list2` are null
    - res = empty list
  - both `list1` and `list2` have same length
    - return merged, sorted list by compareing each list's node values pair by pair
  - `list1` is longer than `list2`
    - once reached end of `list2`, append rest of `list1` to res

## Solution 1: iterative

- O(M + N) T and O(1) S solution
- optional guard clauses
  - return null if both `list1` and `list2` are null
  - return `list1` if `list2` is null
  - return `list2` if `list1` is null
- initialise variables
  - `dummy`: `ListNode` instance that initially points to null
  - `curr`: `ListNode` pointer that initially points to `dummy`
- while `list1` and `list2`:
  - if `list1.val` < `list2.val`:
    - set `list1`'s current node as the next node in the resulting list and update the pointers
    - `curr.next` = `list1`
    - `curr` = `list1`
    - `list1` = `list1.next`
  - else (`list1.val` >= `list2.val`):
    - set `list2`'s current node as the next node in the resulting list and update the pointers
    - `curr.next` = `list2`
    - `curr` = `list2`
    - `list2` = `list2.next`
- if `list1` is null:
  - append the rest of `list2` to the resulting list
  - `curr.next` = `list2`
- if `list2` is null:
  - append the rest of `list1` to the resulting list
  - `curr.next` = `list1`
- return `dummy.next`

## Solution 2: iterative (NeetCode's modded)

- O(M + N) T and O(1) S solution
- same approach as solution 1 iterative but
  - use less pointers and have no guard clauses
  - use less memory due to new list that points directly to the nodes in the original 2 lists instead of creating new nodes in memory

## Solution 3: recursive (OldCodingFarmer's modded)

- O(M + N) T and O(M + N) S solution
- follows recurrence relation
  - `list1[0] + merge(list1[1:], list2) for list1[0] < list2[0]`
  - `list2[0] + merge(list1, list2[1:]) otherwise`
- if either `list1` or `list2` is null
  - return whichever one is not null or null
  - this also covers the case when both lists are null
- if `list1`.val < `list2`.val
  - point `list1`'s next pointer to the result of the recursive call on (`list1`.next, `list2`)
  - return `list1`
- else
  - point `list2`'s next pointer to the result of the recursive call on (`list1`, `list2.next`)
  - return `list2`
