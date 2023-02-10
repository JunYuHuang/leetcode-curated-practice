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
Explanation: ((2 + 1) \* 3) = 9
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

- O(N) time and O(N) space class solution
- stack / array of ints
- hashmap of operator -> lambda(x, y) that returns eval res
  - for Py3, return int(x / y) for division function
- for char in str
  - if char is not in hashmap (char is int)
    - push char to stack
  - else (char is operator)
    - optional = check if stack has 2+ el
    - pop last 2 ints from stack
    - push result of eval of last 2 ints with operator using hashmap
- return stack[0] casted as int
