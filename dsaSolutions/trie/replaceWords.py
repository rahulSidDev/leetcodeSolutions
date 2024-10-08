'''
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's 
call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative 
"helpful". Given a 'dictionary' consisting of many roots and a 'sentence' consisting of words separated by spaces, replace 
all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, 
replace it with the root that has the shortest length. Return the 'sentence' after the replacement.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trieRoot = TrieNode()
        for rootWord in dictionary:
            self.createTrie(rootWord, trieRoot)

        sentenceList = sentence.split(' ')
        for currWord in sentenceList:
            returnVal = self.findWord(currWord, trieRoot)
            sentenceList[sentenceList.index(currWord)] = returnVal
        
        return ' '.join(sentenceList)
    
    def createTrie(self, word, trieRoot):
        node = trieRoot
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        
        node.isWord = True
    
    def findWord(self, word, trieRoot):
        node = trieRoot
        foundPrefix = ''
        for letter in word:
            if letter in node.children:
                foundPrefix += letter
            else:
                return word
            
            if node.children[letter].isWord:
                return foundPrefix
            
            node = node.children[letter]
        
        return word