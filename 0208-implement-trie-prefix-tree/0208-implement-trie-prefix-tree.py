class TrieNode:
    def __init__(self):
        self.node = [None] * 26
        self.is_end = False
class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.trie
        for c in word:
            ord_c = ord(c) - 97
            if curr.node[ord_c]:
                curr = curr.node[ord_c]
            else:
                new_node = TrieNode()
                curr.node[ord_c] = new_node
                curr = curr.node[ord_c]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.trie
        for c in word:
            ord_c = ord(c) - 97
            if curr.node[ord_c]:
                curr = curr.node[ord_c]
            else:
                return False
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr =self.trie
        for c in prefix:
            ord_c = ord(c) - 97
            if curr.node[ord_c]:
                curr = curr.node[ord_c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)