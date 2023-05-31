# O(4^N / sqrt(N)) T and O(4^N / sqrt(N)) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(comb, openN, closedN):
            if openN == n and closedN == n:
                res.append("".join(comb))
                return
            if openN < n:
                comb.append("(")
                backtrack(comb, openN + 1, closedN)
                comb.pop()
            if closedN < openN:
                comb.append(")")
                backtrack(comb, openN, closedN + 1)
                comb.pop()

        backtrack([], 0, 0)

        return res
