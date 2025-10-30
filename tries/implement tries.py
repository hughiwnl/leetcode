class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
Yes — hashmaps store references (pointers) to other objects in memory.
In Python, everything is an object stored somewhere in memory.
Variables (and dictionary values) don’t hold the actual data — they hold a reference (a pointer) to that object’s location.
So in your Trie:
self.children = {}
This dictionary holds:
character → reference to a TrieNode object in memory

cur = cur.children[c]
you’re not copying the node.
You’re saying:
“Follow the pointer stored in children[c] and make cur reference that node’s memory.”
That’s how the algorithm “moves down” the Trie without duplicating anything.
'''