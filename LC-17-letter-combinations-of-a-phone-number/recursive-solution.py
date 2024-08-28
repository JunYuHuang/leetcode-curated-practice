# O(N * 4^N) T and O(N * 4^N) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        res = []
        N = len(digits)
        digToChar = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        def dfs(i = 0, comb = []):
            if i >= N:
                res.append("".join(comb))
                return
            for c in digToChar[digits[i]]:
                comb.append(c)
                dfs(i + 1, comb)
                comb.pop()

        dfs()
        return res