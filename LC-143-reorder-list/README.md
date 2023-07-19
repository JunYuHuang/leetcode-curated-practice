# [LC 143. Reorder List](https://leetcode.com/problems/reorder-list/)

## General Notes

- PEDAC: Problem
  - input:
    - `head`: head `ListNode` of a linked list
      - guaranteed to be not null
    - linked list
      - of size in range \[1, 5 * 10^4]
      - of `ListNode` nodes that have values in range \[1, 1000]
  - output:
    - `res`: new head `ListNode` of the reordered linked list (with the old head `head`)
      - guaranteed to be not null
    - new linked list
      - reordered so sequence alternates between first and last nodes of original lists
      - of size in range \[1, 5 * 10^4]
      - of `ListNode` nodes that have values in range \[1, 1000]
  - constraints
    - cannot modify the values in the linked list
    - can only modify pointers of nodes
  - return `head` if linked list is of size 1 or 2
- PEDAC: Examples
  - TODO

## Solution 1: iterative two-pointer

- My O(N) T and O(1) space solution
- if `head.next` is null, return `head`
- if `head.next.next` is null, return `head`
- define helper function `reverse(node)`
  - reverses the linked list with the head `node`
  - returns the new head of the reversed list
- initialize variables
  - `dummy`: dummy `ListNode` node that points to `head`
  - `slow`: slow pointer that points to `head`
  - `fast`: fast pointer that points to `head`
  - `mid`: pointer that will point to the middle node in the linked list (the `list.size // 2` ith node in a 1-indexed list) with the head node `head` that points initially to null
- find the middle node
  - while `fast` and `fast.next` are not null:
    - `slow` = `slow.next`
    - `fast` = `fast.next.next`
  - `mid` = `slow`
- `curr1` = `dummy.next`
- reverse the 2nd half of the linked list starting from node `mid`
  - `curr2` = `reverse(mid)`
- splice the new resulting list together from the 2 lists made by splitting the original list in half
  - while `curr1` and `curr2` are not null:
    - save the pointers for `curr1.next` and `curr2.next`
      - `next1` = `curr1.next`
      - `next2` = `curr2.next`
    - create the new list by updating the next pointers for `curr1` and `curr2`
      - `curr1.next` = `curr2`
      - `curr2.next` = `next1` if `next1` is not null else `next2`
        - this handles the case for odd-sized linked lists where the 2nd reversed half will always have 1 more node; in this case we want to leave `curr2.next` to point to the last remaining node in the 2nd list `curr2.next`
    - update pointers for `curr1` and `curr2`
      - `curr1.next` = `next1`
      - `curr2.next` = `next2`
- return `dummy.next`

## Solution 2: iterative two-pointer (NeetCode's modded)

- O(N) T and O(1) space solution
- same general approach as solution 1 with some differences
  - no dummy node
  - finding the mid node
    - `slow` pointer = `head`, `fast` pointer = `head.next`
    - mid node of original list is the `list.size // 2 - 1` ith node in a 1-indexed based list i.e. `slow.next` when the loop exists
    - split list by setting `slow.next` to null
  - reversing the 2nd half of the list is done inside the original method (no helper function)
  - when merging the two lists
    - no special case handling since in this case the first half of the split list is always the longer list in an odd-sized list
    - only need to loop while second reversed half head pointer is not null
  - doesn't return anything because problem doesn't require returning anything; only need to modify list in-place
