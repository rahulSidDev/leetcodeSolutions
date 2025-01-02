'''
https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1124/
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramTypes = {}
        
        for i, string in enumerate(strs):
            key = ''.join(sorted(string))  # sorting the string, needs more detailed implementation.
            
            if key not in anagramTypes:
                anagramTypes[key] = [string]
            else:
                anagramTypes[key].append(string)
        
        retArr = []
        
        for anagramKey in anagramTypes:
            retArr.append(anagramTypes[anagramKey])
        
        return retArr