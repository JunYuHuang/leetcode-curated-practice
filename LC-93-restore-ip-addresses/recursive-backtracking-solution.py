# O(3^4 * 4) T and O(3 * 4) S recursive backtracking solution (NeetCode's modded)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        N = len(s)
        if N < 4 or N > 12: return []
        res = []
        def isValidOctet(s): 
            if s[0] == "0": return len(s) == 1
            return int(s) < 256
        
        def backtrack(curr, size, l):
            if l >= N:
                if len(curr) == 4 and size == N:
                    res.append(".".join(curr[:]))
                return
            for r in range(l, min(l + 3, N)):
                if not isValidOctet(s[l:r + 1]): continue
                octet = s[l:r + 1]
                curr.append(octet)
                backtrack(curr, size + len(octet), r + 1)
                curr.pop()
            
        backtrack([], 0, 0)
        return res