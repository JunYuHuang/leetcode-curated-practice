# O(N) T and O(N) S prefix delimiter solution (NeetCode's expl.)
class Codec:
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        N = len(s)
        i = prefL = prefR = 0
        while i < N:
            if '0' <= s[i] <= '9':
                prefR += 1
                i += 1
                continue
            if s[i] == '#':
                size = int(s[prefL:prefR])
                start, end = prefR + 1, prefR + size
                res.append(s[start:end + 1])
                i = prefL = prefR = end + 1
        return res
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
