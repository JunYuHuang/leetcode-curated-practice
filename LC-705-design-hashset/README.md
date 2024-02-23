# [LC 705. Design Hashset](https://leetcode.com/problems/design-hashset/)

## General Notes:

- PEDAC: Problem
  - class methods and inputs
    - `MyHashSet()`: constructor
      - input: none
      - output: a new `MyHashSet` instance
    - `add(key)`
      - input: int `key`
      - output: none
      - does nothing if value `key` is in the hash set
      - adds value `key` to the hash set
    - `remove(key)`
      - input: int `key`
      - output: none
      - does nothing if `key` is not in the hash set
      - removes the value `key` from the hash set
    - `contains(key)`:
      - input: int `key`
      - output: (boolean) true if value `key` is in the hashset else false
  - constraints
    - cannot use any built-in hash table libraries
    - `key` is a value in the range \[0, 10^6]
    - at most 10^4 calls will be made to `add`, `remove`, and `contains`
- PEDAC: Examples
- PEDAC: DS&A

## Solution 1: array and linked list solution (NeetCode's modded)

- method dependent T and S complexity
- summary
  - define a Linked List Node class `Node` that
    - holds an int key `key`
    - has a pointer `next` that points to the next `Node`
  - use linked list to handle hash collisions
  - skip hash set resizing function since we know the max amount of keys that will be stored in the hash set
  - use simple hash function based on hash set's size and the value of the key using the modulus operator
  - `MyHashSet()` constructor
    - initialises an array `store` of size 10^4 where each element is a dummy head `Node` of a linked list
  - `keyToHash(key)` method
    - custom hashing method that returns some 0-indexed int given some non-negative int `key`
    - returns `key` % `store.size`
  - `add(key)` method
    - get the index `pos` of `key` using `keyToHash(key)`
    - traverse the linked list at `store[pos]` with the pointer `curr`
      - if there is a node with key value equal to `key`,
        - return
    - append a new node with key value `key` to the end of the list
  - `remove(key)` method
    - get the index `pos` of `key` using `keyToHash(key)`
    - traverse the linked list at `store[pos]` with the pointer `curr`
      - if there is a node `curr.next` with key value equal to `key`,
        - connect the nodes `curr` and `curr.next.next` via their pointers so that `curr.next` is dereferenced (has nothing point to it)
        - retur
  - `contains(key)` method
    - get the index `pos` of `key` using `keyToHash(key)`
    - traverse the linked list at `store[pos]` with the pointer `curr`
      - if there is a node with key value equal to `key`,
        - return true
    - return false
