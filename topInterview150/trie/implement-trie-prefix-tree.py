'''
https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=top-interview-150
'''
class TrieNode:
    def __init__(self):
        # variables to store whether the current node makes up the end of a word or not, and to store
        # the children to the current node.
        self.isword = False
        self.children = {}

class Trie:

    def __init__(self, val=None, children={}):
        # instance variable to store the root of the trie. 
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # initialise the starting node to be the root node of the trie.
        node = self.root

        # iterate over each letter in the input word string.
        for i in word:
            # if the current letter is not in the dictionary of node children then create a node for
            # the letter and add it to the node's children dict.
            if i not in node.children:
                node.children[i] = TrieNode()
            
            # otherwise update the node to the child node that matches the current letter.
            node = node.children[i]
        
        # after the insertion of the word is done mark the last node as a valid word.
        node.isword = True

    def search(self, word: str) -> bool:
        # initialise the starting node to be the root node of the trie.
        node = self.root

        # iterate over each letter in the input word string.
        for i in word:
            # if at any point the current letter is not found to be in the current node's children.
            # then that means that the input word doesn't exist and false is returned.
            if i not in node.children:
                return False
            
            # if the current letter exists in the children then update the node to the child that matches.
            node = node.children[i]
        
        # return whether the last node is a word or not.
        return node.isword

    def startsWith(self, prefix: str) -> bool:
        # intialise the starting node to be the root node.
        node = self.root

        # iterate over each letter in the input word string.
        for i in prefix:
            # if at any point the current letter is not found to be in the current node's children.
            # then that means that the prefix doesn't exist and false is returned.
            if i not in node.children:
                return False
            
            # if the current letter exists in the children then update the node to the child that matches.
            node = node.children[i]
        
        # if the end of the prefix is reached then that means there exists a word with the prefix and so 
        # true is returned.
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
