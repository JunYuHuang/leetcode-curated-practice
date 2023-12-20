# [LC 1472. Design Browser History](https://leetcode.com/problems/design-browser-history/)

## General Notes

- PEDAC: Problem
  - class methods and inputs
    - `BrowserHistory(homepage)`: constructor
      - input: string `homepage`
      - output: a new `BrowserHistory` instance
    - `visit(url)`
      - input: string `url`
      - output: none
      - visits `url` from current page and clears all forward history
    - `back(steps)`:
      - input: int `steps`
      - output: string that is the current `url` after moving back in history at most `steps` times
      - goes back `min(steps, x)` where `x` is the count of entries in the history
    - `forward(steps)`:
      - input: int `steps`
      - output: string that is the current `url` after moving forward in history at most `steps` times
      - goes forward `min(steps, x)` where `x` is the count of entries in the history
  - constraints
    - `homepage`, `url`: strings of chars of `.` and lowercase English letters
      - of size in range \[`1`, `20`]
    - at most 5000 calls will be made to all non-constructor class methods

## Solution 1: stack solution

- For time and space complexity, see individual methods
  - where N = count of nodes in the list
  - `visit(url)`: O(N) T
  - `back(steps)`: O(N) T
  - `forward(steps)`: O(N) T
- `BrowserHistory(homepage)` constructor that sets the following instance fields:
  - `stack`: stack that holds elements of `[index, url]` initially set to an array of size 1 with element `[0, homepage]`
  - `currPos`: int pointer initially set to 0 that represents the browser's current page's index in `stack`
- `visit(url)`
  - while `stack` is not empty and `stack[-1][0]` > `currPos`:
    - pop last el from `stack`
  - push [`currPos` + 1, `url`] to `stack`
  - `currPos++`
- `back(steps)`
  - `backSteps`: `min(currPos, steps)`
  - while `backSteps` > 0:
    - `currPos--`
    - `backSteps--`
  - return `stack[currPos][1]`
- `forward(steps)`
  - `maxStepsForward`: `stack`.size - 1 - `currPos`
  - `forwardSteps`: `min(maxStepsForward, steps)`
  - while `forwardSteps` > 0:
    - `currPos++`
    - `forwardSteps--`
  - return `stack[currPos][1]`

## Solution 2: doubly linked list solution

- For time and space complexity, see individual methods
  - where N = count of nodes in the list
  - `visit(url)`: O(1) T
  - `back(steps)`: O(N) T
  - `forward(steps)`: O(N) T
- same concept as solution 1 but:
  - replace stack of `[index, url]` elements with doubly linked list of nodes with fields `val`, `prev`, and `next`
  - constructor initialises with 3 fields
    - `left`: dummy node point to start of linked list
    - `right`: dummy node pointing to end of linked list
    - `curr`: pointer that points to current visited page in list
  - `visit(url)`
    - instead of having to pop all elements before the current page, just need to update pointers for `curr`, `right`, and for the newly created node
  - `backward(steps)`:
    - keep moving `curr` pointer backward only if `steps` > 0 and `curr` is not null and `curr.prev` is not `left`
  - `forward(steps)`:
    - keep moving `curr` pointer forward only if `steps` > 0 and `curr` is not null and `curr.next` is not `right`
