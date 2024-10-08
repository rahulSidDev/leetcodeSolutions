'''
You are given a 0-indexed array of unique strings 'words'. A palindrome pair is a pair of integers '(i, j)' such that:
1. 0 <= i, j < words.length
2. i != j
3. words[i] + words[j]. (the concatenation of the two strings) is a palindrome.
Return an array of all the palindrome pairs of 'words'.
You must write an algorithm with 'O(sum of words[i].length)' runtime complexity.
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):
            
            if word in backward and backward[word] != i:
                res.append([i, backward[word]])
                
            if word != "" and "" in backward and word == word[::-1]:
                res.append([i, backward[""]])
                res.append([backward[""], i])
                
            for j in range(len(word)):
                if word[j:] in backward and word[:j] == word[j-1::-1]:
                    res.append([backward[word[j:]], i])
                if word[:j] in backward and word[j:] == word[:j-1:-1]:
                    res.append([i, backward[word[:j]]])
                    
        return res