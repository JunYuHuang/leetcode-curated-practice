# O(N) T and O(N) S stack solution (NeetCode's modded)
class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for c in s:
            if c in closeToOpen: # c is a closed parentheses char
                if stack and stack[-1] == closeToOpen[c]: stack.pop()
                else: return False
            else: # c is a open parentheses char
                stack.append(c)
        return not stack
