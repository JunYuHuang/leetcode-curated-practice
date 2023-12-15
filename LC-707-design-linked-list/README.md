# [LC 707. Design Linked List](https://leetcode.com/problems/design-linked-list/description/)

## General Notes

- PEDAC: Problem
  - class methods and inputs
    - `MyLinkedList()`: constructor
      - output: a new `MyLinkedList` instance
    - `get(index)`
      - input: int `index`
      - output: returns the value of the `index`th node if it exists else `-1` if `index` is invalid
    - `addAtHead(val)`
      - input: int `val`
      - output: null
      - adds a node of value `val` before the first element of the list
      - newly added node becomes new head of list
    - `addAtTail(val)`
      - input: int `val`
      - output: null
      - adds a node of value `val` to the list's end as its last element
    - `addAtIndex(index, val)`
      - input: int `index`, int `val`
      - output: null
      - does nothing if `index` is invalid (equal to -1 or length of list)
      - adds a node of value `val` before the `index`th node in the list
    - `deleteAtIndex(index)`
      - input: int `index`
      - output: null
      - does nothing if `index` is invalid (equal to -1 or length of list)
      - deletes the `index` node in the list
  - constraints
    - list is 0-indexed
    - `index`: int in range \[0, 1000]
    - `val`: int in range \[0, 1000]
    - cannot use built-in LinkedList library
    - at most 2000 calls will be made to all non-constructor class methods

## Solution 1: singly linked list solution

- For time and space complexity, see individual methods
  - where N = count of nodes in the list
  - `get(index)`: O(N) T
  - `addAtHead(val)`: O(N) T
  - `addAtTail(val)`: O(N) T
  - `addAtIndex(index, val)`: O(N) T
  - `deleteAtIndex(index)`: O(N) T
- summary notes
  - define `Node` class for singly linked list with `val` and `next` fields
  - define fields `dummyHead` and `size` fields for `MyLinkedList` class

## Solution 2: doubly linked list solution (NeetCode's modded)

- For time and space complexity, see individual methods
  - where N = count of nodes in the list
  - `get(index)`: O(N) T
  - `addAtHead(val)`: O(1) T
  - `addAtTail(val)`: O(1) T
  - `addAtIndex(index, val)`: O(N) T
  - `deleteAtIndex(index)`: O(N) T
- summary notes
  - define `Node` class for doubly linked list with
    - int `val` field
    - `Node` `prev` pointer field
    - `Node` `next` pointer field
  - define my `MyLinkedList` class
    - `Node` `left` field that is a dummy node that points to the list's head node if it exists else `right`
    - `Node` `right` field that is a dummy node that points to the list's tail node if it exists else `left`
  - update `next` and `prev` pointers for `left` and `right` dummy nodes on list mutation (add or remove operations)
