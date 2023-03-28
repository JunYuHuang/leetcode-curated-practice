# O(logK) T and O(N) S recursive solution (repititionismastery's modded)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        if k % 2: # k is odd
            return self.kthGrammar(n - 1, (k + 1) / 2)
        else: # k is even
            return self.flip(self.kthGrammar(n - 1, k / 2))
    def flip(self, val): return 1 if val == 0 else 0