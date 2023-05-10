# O(N * M) T and O(N * M) S hashmap solution (NeetCode's modded)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        startOrd = ord("a")
        COUNT_LEN = 26
        for s in strs:
            count = [0] * COUNT_LEN
            for c in s:
                pos = ord(c) - startOrd
                count[pos] += 1
            count = tuple(count)
            res[count] = res.get(count, [])
            res[count].append(s)
        return res.values()
