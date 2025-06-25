'''
https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the lengths of the input strings are not the same then there are extra 
        # letters present in either of the strings and this ensures that the input strings
        # are not anagrams.
        if len(s) != len(t):
            return False

        # hashmap to store the occurence of letters in string 's'.
        letterOccurence = {}

        for ele in s:
            # iterate over each char in 's' and if it is not present in the hashmap then add it
            # with occurence no. 1. otherwise increment the char occurence by 1.
            if ele not in letterOccurence:
                letterOccurence[ele] = 1
            else:
                letterOccurence[ele] += 1
        
        for ele in t:
            # iterate over each char in string 't'. if current char is not present in the hashmap then that means
            # it is not present in the string 's' and both 's' and 't' are not anagrams. so false is returned.
            if ele not in letterOccurence:
                return False
            
            # decrement the occurence of current char of 't' in the hashmap by 1.
            letterOccurence[ele] -= 1
            # if the occurence of current character drops below zero then that means 't' has extra chars which also
            # occur in 's'. this makes 's' and 't' not anagrams and so false is returned.
            if letterOccurence[ele] < 0:
                return False
        
        # after all checks are done and false is not returned means that 's' and 't' are anagrams
        # and true is returned.
        return True
