# Description

## [LC 150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

Medium

You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return _an integer that represents the value of the expression_.

**Note** that:

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a **32-bit** integer.

Example 1:

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

Example 2:

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

Example 3:

```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 _ (6 / ((9 + 3) _ -11))) + 17) + 5
= ((10 _ (6 / (12 _ -11))) + 17) + 5
= ((10 _ (6 / -132)) + 17) + 5
= ((10 _ 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

Constraints:

- `1 <= tokens.length <= 104`
- `tokens[i]` is either an operator: `'+'`, `'-'`, `'*'`, or `'/'`, or an integer in the range `[-200, 200]`.

# Solutions

## Solution 1: stack

- O(N) time and O(N) space solution
- initialise variables
  - `nums`: empty int list
  - `opToFn`: hashmap that maps each of the 4 arithmetic operators to a lambda function that takes in `(l, r)` ints and returns the evaluated result
- loop thru every char `c` in string `tokens`
  - if `c` is a int (not in `opToFn` dict)
    - push `c` converted to an int to `nums`
  - else if `nums` has 2+ ints
    - `left` = pop from `nums`
    - `right` = pop from `nums`
    - `res` = `opToFn[c](left, right)`
    - push `res` to `nums`
- return `nums[0]`
