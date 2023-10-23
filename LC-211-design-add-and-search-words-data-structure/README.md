# [LC 211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/)

## General Notes

- PEDAC: Problem
  - class methods and inputs
    - `WordDictionary()`: constructor
      - input: none
      - output: a new `WordDictionary` instance / object
    - `addWord(word)`
      - input: string `word`
        - of size in range \[1, 25]
        - of only lowercase English chars
      - output: none
    - `search(word)`
      - input: string `word`
        - of size in range \[1, 25]
        - of only lowercase English chars or at most 2 `.` dot chars
      - output: boolean true if `word` has been added previously else false

## Solution 1: trie solution (NeetCode's modded)

- method-dependent T & S complexity solution
  - where N = number of words
  - where M = length of `word`
  - `addWord()`: O(M) T and O(M) S
  - `search()`: O(max(M, N * 26^M)) T and O(max(1, M)) S
- summary
  - implement `TrieNode` class where the constructor
    - has a `children` instance variable that is set to an empty hashmap but when non-empty stores a hashmap of other `TrieNode` objects
    - has a `isWordEnd` boolean instance variable that indicates if the current node is the end of a word
  - `WordDictionary` initialises with
    - an instance variable `root` that points to a new `TrieNode` instance
    - an int instance variable `maxLen` set to 0 that is maintained to keep the maximum length of any inserted word
  - `addWord(word)`: creates or traverses or updates `M` (length of `word`) `TrieNode` objects attached to `root`
  - `searchWord(word)`:
    - return false if size of `word` > `maxLen`
    - `currNode`: point set to `root`
    - define `dfs(currNode, i)` recursive helper method
      - loop thru every char `c` in `word` starting from index `i`:
        - if `c` is a `.` (dot) char:
          - loop thru every `key`, `value` in `currNode.children`:
            - if `dfs(value, i + 1)` returns true:
              - return true
        - else if `c` is a key in `currNode.children`:
          - `currNode` = `currNode.children[c]`
        - else:
          - return false
      - return `currNode.isWordEnd`
