# O(maxK * countK * N) time and (maxK * countK * N) space stack solution (NeetCode's modified)
class Solution:
    def decodeString(self, s: str) -> str:
        def isDigit(c): return '0' <= c <= '9'
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
                continue
            temp = [] # stores curr sub problem / str
            while stack and stack[-1] != "[":
                temp.append(stack.pop())
            stack.pop() # remove the [ char
            times, i = 0, 0
            while stack and isDigit(stack[-1]):
                times += int(stack.pop()) * (10 ** i)
                i += 1
            res = times * "".join(temp[::-1])
            stack.append(res)
        return "".join(stack)