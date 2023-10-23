# Method-dependent T & S complexity trie solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.maxLen = 0

    def addWord(self, word: str) -> None:
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]
        curNode.isWordEnd = True
        if len(word) > self.maxLen: self.maxLen = len(word)

    def search(self, word: str) -> bool:
        if len(word) > self.maxLen: return False

        def dfs(curNode, pos):
            for i in range(pos, len(word)):
                c = word[i]
                if c == ".":
                    for child in curNode.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
                elif c in curNode.children:
                    curNode = curNode.children[c]
                else:
                    return False
            return curNode.isWordEnd
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
