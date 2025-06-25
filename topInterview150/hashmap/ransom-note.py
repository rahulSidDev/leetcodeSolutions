'''
https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # hashmap to store the count of letters in magazine
        countDict = {}

        for letter in magazine:
            # store 1 in hashmap if the letter is not already there in the hashmap
            # otherwise just increment the letter's count.
            if letter not in countDict:
                countDict[letter] = 1
            else:
                countDict[letter] += 1
        
        for letter in ransomNote:
            # if any letter in ransomNote is not present in magazine then creating ransomNote
            # from magazing is not possible and false is returned.
            if letter not in countDict:
                return False
            
            # decrement the count of current letter in the hashmap.
            countDict[letter] -= 1
            # if the count of a letter falls below 0 in the hashmap then that means the letters
            # in magazine are not enough to create the ransomNote, and so false is returned.
            if countDict[letter] < 0:
                return False
        
        # if none of the previous hiccups are encountered then return True.
        return True
