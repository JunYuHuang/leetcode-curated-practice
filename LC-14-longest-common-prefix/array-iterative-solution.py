# NeetCode's iterative array O(m * n) T + O(n) S modded solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strsLen = len(strs)
        if strsLen == 1:
            return strs[0]
        
        firstLen = len(strs[0])
        res = []
        for i in range(firstLen):
            for j in range(1, strsLen):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return "".join(res)
            res.append(strs[0][i])
        
        return "".join(res)
