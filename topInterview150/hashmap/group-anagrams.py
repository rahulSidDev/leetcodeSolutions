'''
https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap to store each kind of anagram.
        anagramTypes = {}
        
        for i, string in enumerate(strs):
            # iterate over each string in the input list. for each string create a key by sorting the 
            # letters of current string. since anagrams contain the same letters just in different order,
            # sorting each anagram's letters should result in the same key. and so each anagram can be stored
            # under the same key in the hashmap
            key = ''.join(sorted(string))
            
            if key not in anagramTypes:
                # if the key is not present in the hashmap then add it to the map by mapping it to the list
                # containing the current string.
                anagramTypes[key] = [string]
            else:
                # if the key is present then append the string to the list associated with the key.
                anagramTypes[key].append(string)
        
        # create an empty list to store the result to return it.
        retArr = []
        for anagramKey in anagramTypes:
            # iterate over each anagram key in the hashmap and append all the lists associated
            # with each key into the return list. this will build up the return list.
            retArr.append(anagramTypes[anagramKey])
        
        # return the final list with the right answer.
        return retArr
