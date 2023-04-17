# O(N * 4^N) T and O(N * 4^N) S recursive backtracking solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res, N = [], len(digits)
        digitToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(curr, i):
            if i == N:
                res.append("".join(curr[:]))
                return
            for c in digitToLetters[digits[i]]:
                curr.append(c)
                backtrack(curr, i + 1)
                curr.pop()
        backtrack([], 0)
        return res