'''
https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # convert the pattern and s strings into lists of letters and words respectively.
        pattern = list(pattern)
        s = s.split()

        # if the lengths of both input strings are not the same then return false as they
        # don't follow the same pattern. this is because there will be extra words or letters
        # that don't map to anything.
        if len(pattern) != len(s):
            return False

        # hashmaps to store mappings from letter to word and mappings from word to letters.
        letter_to_word = {}
        word_to_letter = {}
        # 'n' is the length of 's' or 'pattern' whichever is lesser. it is used for iteration.
        n  = min(len(s), len(pattern))

        for i in range(n):
            # if the current letter in pattern is present in the first hashmap and it doesn't
            # map to the current word in string 's' then that means the current letter maps to 
            # two different words and the input strings don't follow the same pattern. so false is returned.
            if pattern[i] in letter_to_word and letter_to_word[pattern[i]] != s[i]:
                return False

            # same logic as above but the strings swapped and the second hashmap used.
            if s[i] in word_to_letter and word_to_letter[s[i]] != pattern[i]:
                return False
            
            # add a mapping of current word to current letter in the second hashmap.
            word_to_letter[s[i]] = pattern[i]
            # do the same but vice versa in the first hashmap.
            letter_to_word[pattern[i]] = s[i]
        
        # if no mappings to different words or letters are found then the input strings
        # follow the same pattern and true is returned.
        return True
