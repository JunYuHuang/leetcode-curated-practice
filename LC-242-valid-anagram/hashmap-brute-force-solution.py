# O(S + T) T and O(26) S hashmap brute force solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        charToCount = {}
        for c in s:
            charToCount[c] = charToCount.get(c, 0) + 1
        for c in t:
            if c not in charToCount: return False
            charToCount[c] -= 1
            if charToCount[c] < 0: return False
        for c in charToCount:
            if charToCount[c] != 0: return False
        return True
