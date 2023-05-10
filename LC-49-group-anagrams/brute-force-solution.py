# O(N * MLogM) T and O(N * M) S brute force sort solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sSorted = "".join(sorted([c for c in s]))
            res[sSorted] = res.get(sSorted, [])
            res[sSorted].append(s)
        return res.values()
