'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys 
in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
-> 'Trie()' Initializes the trie object.
-> 'void insert(String word)' Inserts the string 'word' into the trie.
-> 'boolean search(String word)' Returns 'true' if the string 'word' is in the trie (i.e., was inserted before), and 
'false' otherwise.
-> 'boolean startsWith(String prefix)' Returns 'true' if there is a previously inserted string 'word' that has the prefix 
'prefix', and 'false' otherwise.
'''
class TrieNode:
    def __init__(self):
        self.isword = False
        self.children = {}

class Trie:

    def __init__(self, val=None, children={}):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.isword = True

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.isword

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True