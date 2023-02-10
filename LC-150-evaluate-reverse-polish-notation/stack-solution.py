# My O(N) time and O(N) space stack solution
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operatorToFunc = { 
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        stack = []
        for c in tokens:
            if c not in operatorToFunc: stack.append(int(c)) # is int
            else: # is operator
                second = stack.pop()
                first = stack.pop()
                res = operatorToFunc[c](first, second)
                stack.append(res)
        return stack[0]