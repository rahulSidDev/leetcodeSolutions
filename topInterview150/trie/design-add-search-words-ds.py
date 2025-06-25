'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/description/?envType=study-plan-v2&envId=top-interview-150
'''
class TrieNode:
    def __init__(self):
        # instance variables to store the child nodes and whether the current node is a word or not.
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        # instance var to store the root of the trie.
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        # initialise the starting node to be the root of the trie.
        node = self.trieRoot

        # iterate over each letter in the word.
        for letter in word:
            # if the letter is not found in the node's children then add it.
            if letter not in node.children:
                node.children[letter] = TrieNode()

            # move the node onto the next child node that matches the letter.
            node = node.children[letter]
        
        # return whether the end node is a valid word or not.
        node.isWord = True

    def search(self, word: str) -> bool:
        def recurHelper(node, ind):
            # if the current index is the last one in the word then return whether the last node
            # is a valid word or not.
            if ind == len(word):
                return node.isWord
            
            # if the current letter at index is a dot, then it could match any of the letters. and so
            # all child nodes are iterated over and checked whether they match the next letter or not.
            if word[ind] == '.':
                for child in node.children:
                    # if the next letter matches then return true and end the iteration.
                    if recurHelper(node.children[child], ind+1):
                        return True
            
            # if the current letter is in the child nodes of the current node then iterate over the next
            # letter from word on the child node that matches.
            if word[ind] in node.children:
                return recurHelper(node.children[word[ind]], ind+1)
            
            # return false if the letter doesn't exist in the child nodes.
            return False
        
        # run the helper function by passing in root and 0 as index. return the answer returned from the
        # helper function.
        return recurHelper(self.trieRoot, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
