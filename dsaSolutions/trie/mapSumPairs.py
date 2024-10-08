'''
Design a map that allows you to do the following:
-> Maps a string key to a given value.
-> Returns the sum of the values that have a key with a prefix equal to a given string.
Implement the 'MapSum' class:
->	'MapSum()' Initializes the 'MapSum' object.
->	'void insert(String key, int val)' Inserts the 'key-val' pair into the map. If the 'key' already existed, the 
	original 'key-value' pair will be overridden to the new one.
->	'int sum(string prefix)' Returns the sum of all the pairs' value whose 'key' starts with the 'prefix'.
'''
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        curr = self.root
        curr.score += delta
        
        for char in key:
            curr = curr.children.setdefault(char, TrieNode())
            curr.score += delta

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.score