# [LC 146. LRU Cache](https://leetcode.com/problems/lru-cache/description/)

## General Notes

- PEDAC: Problem
  - class methods and inputs
    - `LRUCache(capacity)`: constructor
      - input: int `capacity`
      - output: a new `LRUCache` instance
    - `get(key)`
      - input: string `word`
      - output: an int value associated with `key` or -1 if `key` doesn't exist
    - `put(key, value)`
      - input: string `word`
      - output: none
  - constraints
    - `capacity`: int in range \[1, 3000]
    - `key`: int in range \[0, 10^4]
    - `value`: int in range \[0, 10^5]

## Solution 1: (doubly) linked list solution

- O(1) T and O(1) S for all methods
- summary
  - create `Node` class whose constructor has the following fields:
    - `key`, `val`, `prev`, `next`
  - use a doubly linked list to represent LRU cache with dummy head `left` (points to LRU node) and tail `right` (points to MRU node) nodes that point to each other
  - set an instance int var `cap` equal to `capacity`
  - MRU = Most Recently Used
  - use a hashmap `cache` that maps each int `key` to a pointer that points to its associated node in the linked list
  - `get()` method calls modify the list
    - if associated node exists, it becomes the MRU node
      - remove it from the list
      - insert it back to the list as the new tail (MRU) node
  - `put()` method calls modify the list and hashmap
    - if associated node exists, remove it from the list
    - create a new node with the given `key` and `value`
    - insert it to the list as the new tail (MRU) node
    - add or update its node pointer for its associated key in `cache`
    - if `cache` has exceeded capacity,
      - remove the LRU node pair from both the list and `cache` dict
- `remove(node)`: helper method that removes a node from the list
  - `prev` = `node.prev`
  - `nxt` = `node.next`
  - `prev.next` = null
  - `nxt.prev` = null
- `insert(node)`: helper method that inserts a node as the new non-dummy tail MRU node
  - `prev` = `right.prev`
  - `nxt` = `right`
  - `prev.next` = `node`
  - `nxt.prev` = `node`
  - `node.prev` = `prev`
  - `node.next` = `nxt`
- `get(key)` method
  - returns -1 if `key` is not in `cache`
  - `remove(cache[key])`
  - `insert(cache[key])`
  - return `cache[key].val`
- `put(key, value)` method
  - if `key` IS in `cache`,
    - `remove(cache[key])`
  - `newNode` = `Node(key, value)`
  - `insert(newNode)`
  - add `(key, newNode)` pair to `cache`
  - if cache is at capacity (`cache.size >= cap`), evict the LRU node
    - `lru` = `left.next`
    - `remove(lru.key)`
    - delete `(lru.key, lru)` pair from `cache`
