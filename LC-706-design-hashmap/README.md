# [LC 706. Design HashMap](https://leetcode.com/problems/design-hashmap/)

## General Notes:

- PEDAC: Problem
  - class methods and inputs
    - `MyHashMap()`: constructor
      - input: none
      - output: a new `MyHashMap` instance
      - creates an empty hashmap `map` internally
    - `put(key, value)`
      - input: int `key`, int `value`
      - output: none
      - if `key` is not a key in `map`,
        - inserts the `(key, value)` pair in `map`
      - else,
        - update the `value` associated with `key` in the map
    - `get(key)`:
      - input: int `key`
      - output:
        - if `key` is a key in `map`,
          - the int `value` associated with `key`
        - else -1
    - `remove(key)`:
      - input: int `key`
      - output: none
      - if `key` is a key in `map`,
        - delete both `key` and its associated value from `map`
      - else, do nothing
  - constraints
    - cannot use any built-in hash table libraries
    - `key`, `value` are values in the range \[0, 10^6]
    - at most 10^4 calls will be made to `add`, `remove`, and `contains`
- PEDAC: Examples
- PEDAC: DS&A

## Solution 1: array and linked list solution (NeetCode's modded)

- method dependent T and S complexity
- summary
  - define `ListNode` class
    - with fields int `key`, int `value`, ListNode `next`
  - `MyHashMap` class
    - constructor
      - creates an array `store` of `ListNode` dummy nodes of size 10^4
    - `keyToHash(key)` method
      - hash function = `key` % size of `store`
    - `put(key, value)` method
      - get index `pos` via `keyToHash(key)`
      - traverse list at `store[pos]` with `curr` pointer
        - if node `curr.next.key` == `key`,
          - update this node's `value` prop with `value`
          - return
        - go to the next node
      - append new `ListNode` with `(key, value)` at end of the list
    - `get(key)`
      - get index `pos` via `keyToHash(key)`
      - traverse list at `store[pos]` with `curr` pointer
        - if node `curr.next.key` == `key`,
          - return `curr.next.value`
        - go to the next node
      - return -1
    - `remove(key)`
      - get index `pos` via `keyToHash(key)`
      - traverse list at `store[pos]` with `curr` pointer
        - if node `curr.next.key` == `key`,
          - update the connection between `curr` and `curr.next.next` via their `next` pointers so that `curr.next` is dereferenced
          - return
        - go to the next node
