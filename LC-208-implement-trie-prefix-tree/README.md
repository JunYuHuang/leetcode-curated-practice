# [LC 208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

## General Notes

- PEDAC: Problem
  - class methods and inputs
    - `Trie()`: constructor
      - input: none
      - output: a new `Trie` instance / object
    - `insert(word)`
      - input: string `word`
      - output: none
    - `search(word)`
      - input: string `word`
      - output: boolean true if the exact string `word` is in the trie else false
    - `startsWith(prefix)`
      - input: string `prefix`
      - output: boolean true if there are 1+ strings prefixed with the string `prefix` or if the exact string `prefix` is in the trie
  - constraints
    - `word`, `prefix`
      - string
      - of size in the range \[1, 2000]
      - of char values that are lowercase English letter chars

## Solution 1: trie solution

- For time and space complexity, see individual methods
  - where N = size of `word` or `prefix`
  - where M = max length of the word or prefix
  - `Trie()`: O(M * N) S
  - `insert(word)`: O(M) T and O(M) S
  - `search(word)`, `startsWith(prefix)`: O(M) T and O(1) S
- create `Node` class that represents the `char` of each word
- `Node` class attributes and methods
  - `isWordEnd`: boolean that is `true` if this `Node` is the end of a word else false
  - `children`: a hashmap of `Node` objects
- `Trie()`:
  - create instance variable `root` set to a `Node` object
- `insert(word)`:
  - create a "linked list" of `Node` objects starting from the first char in `word` (stored in `self.root`) to the end of it
  - if any `Node` object as part of the "linked list" already exists, do not recreate it
  - for the last `Node` that represents the last char of `word`, set its `isWordEnd` to true
- `search(word)`:
  - `curr`: pointer that points to current `Node` traversed set initially to `self.root`
  - for each char `c` with index `i` in `word`,
    - if `curr.children[c]` is null, return false
    - if is last char (`i` == size of `word` - 1),
      - return `curr.isWordEnd`
    - `curr` = `curr.children[c]`
- `startsWith(prefix)`:
  - `curr`: pointer that points to current `Node` traversed set initially to `self.root`
  - for each char `c` with index `i` in `prefix`,
    - if `curr.children[c]` is null, return false
    - `curr` = `curr.children[c]`
  - return true
