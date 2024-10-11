# O(4^N * N) T and O(4^N * N) S recursive dfs solution (NeetCode's modded)
class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        N = len(digits)
        res = []
        digToChars = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        def dfs(i, comb):
            if i >= N:
                res.append("".join(comb))
                return
            for char in digToChars[digits[i]]:
                comb.append(char)
                dfs(i + 1, comb)
                comb.pop()

        dfs(0, [])
        return res
