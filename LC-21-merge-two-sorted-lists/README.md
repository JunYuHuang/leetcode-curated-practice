# [LC 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## General Notes

- PEDAC: Problem
  - input: 
    - `list1`: head of list that may be null
    - `list2`: head of list that may be null
  - output: head ListNode of sorted merged list that may be null
  - both lists are sorted in non-decreasing order

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

- O(N) time and O(N) space solution
- if both heads of `list1` and `list2` are null, return null
- if head of `list1` is null, return head of `list2`
- if head of `list2` is null, return head of `list1`
- initialise variables
  - dummy node
  - curr node pointer that points to dummy
  - head1 and head2 that point to heads of each list respectively
- while both head1 and head2 are not null
  - if head1.val < head.2val
    - append new node created from head1.val to curr.next
    - point to next node in `list1`
  - else
    - append new node created from head2.val to curr.next
    - point to next node in `list2`
  - curr = curr.next
- if head1 is not null, append rest of `list1` to end of curr
- if head2 is not null, append rest of `list2` to end of curr
- return dummy.next

## Solution 2: iterative (NeetCode's modded)

- O(N) time and O(1) space solution
- same approach as solution 1 iterative but
  - use less pointers and have no guard clauses
  - use less memory due to new list that points directly to the nodes in the original 2 lists instead of creating new nodes in memory

## Solution 3: recursive (OldCodingFarmer's modded)

- O(N) time and O(N) space solution
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