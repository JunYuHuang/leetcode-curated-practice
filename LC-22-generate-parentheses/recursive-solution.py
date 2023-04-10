# O(4^N / sqrt(N)) T and O(4^N / sqrt(N)) S solution (NeetCode's modded)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, openN, closedN):
            if len(curr) == n * 2:
                res.append("".join(curr))
                return
            if openN < n:
                curr.append("(")
                backtrack(curr, openN + 1, closedN)
                curr.pop()
            if closedN < openN:
                curr.append(")")
                backtrack(curr, openN, closedN + 1)
                curr.pop()
        backtrack([], 0, 0)
        return res