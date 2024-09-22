class TrieNode:
    def __init__(self, word_end=False):
        self.children=[None]*26
        self.word_end=word_end
class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        # traverse the root and add children if does not exist
        tmp = self.root
        for c in word:
            pos = ord(c)-ord('a')
            if not tmp.children[pos]:
                tmp.children[pos]=TrieNode()
            tmp=tmp.children[pos]
        tmp.word_end=True
        
    def search(self, word: str) -> bool:
        tmp=self.root
        for c in word:
            pos = ord(c)-ord('a')
            if not tmp.children[pos]:
                return False
            tmp=tmp.children[pos]
        return tmp.word_end

    def startsWith(self, prefix: str) -> bool:
        tmp=self.root
        for c in prefix:
            pos = ord(c)-ord('a')
            if not tmp.children[pos]:
                return False
            tmp=tmp.children[pos]
        return True

if __name__=='__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))