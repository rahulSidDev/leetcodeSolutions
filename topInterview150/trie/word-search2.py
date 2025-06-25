'''
https://leetcode.com/problems/word-search-ii/description/?envType=study-plan-v2&envId=top-interview-150
'''
class TrieNode:
    def __init__(self):
        # instance variables to store the children and the end node in a trie.
        self.children = {}
        self.end_node = 0

class Trie:
    def __init__(self):
        # intance variable to store the root of the trie.
        self.root = TrieNode()

    def insert(self, word):
        # initialise the starting node to the root of the trie.
        root = self.root

        # iterate over each letter in the word.
        for symbol in word:
            # add the current letter into the dict of children of the current node.
            root = root.children.setdefault(symbol, TrieNode())
        
        # after the word has been inserted assign 1 to the end node variable to show that the last
        # added node constitutes a valid word.
        root.end_node = 1

class Solution:
    def findWords(self, board, words):
        # store the no. of word in the input list.
        self.num_words = len(words)

        # the 'res' list will have the resulting words. 'trie' is an object of the trie class.
        res, trie = [], Trie()

        # itearate over all the words in the list and insert them one by one into the trie.
        for word in words: trie.insert(word) 

        # iterate over all the squares over the board and perform the dfs search on the trie for each square.
        for i in range(len(board)):
            for j in range(len(board[0])):
                # call the dfs function by passing the board, the root of the trie, i and j as the indices for
                # the board, empty string as the initial path, and the result list.
                self.dfs(board, trie.root, i, j, "", res)
        
        # return the result list which will hold all the words found on the board.
        return res

    def dfs(self, board, node, i, j, path, res):
        # if the no. of words is 0 then return none as there is nothing to search on the board.
        if self.num_words == 0: return

        # if the current node is the end node then we've reached the end of a word. in this case append
        # the path to the result list, mark the end node as the false so that the same word is not added in
        # the resulting string again, and reduce the no. of words by 1.
        if node.end_node:
            res.append(path)
            node.end_node = False
            self.num_words -= 1

        # if either i or j go out of bounds of the board then return none.
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return

        # store the letter in the current square on the board. and if its not present in the children
        # of the current node then return none as it cannot be a part of a valid word. 
        tmp = board[i][j]
        if tmp not in node.children: return

        # if the letter is present in the children of the current node then mark it as hash to ensure 
        # that it is not considered more than once for the same word.
        board[i][j] = "#"
        # perform the dfs for each square left, right, bottom, and top of the current square.
        for x,y in [[0,-1], [0,1], [1,0], [-1,0]]:
            self.dfs(board, node.children[tmp], i+x, j+y, path+tmp, res)
        
        # add the letter back onto the board for future word matches.
        board[i][j] = tmp
