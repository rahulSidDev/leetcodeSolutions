'''
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
'''
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {}
        
        for i in range(len(list1)):
            hashmap[list1[i]] = i
        
        hashmap2 = {}
        
        for i in range(len(list2)):
            if list2[i] in hashmap:
                hashmap2[list2[i]] = hashmap[list2[i]] + i
        
        minIndSum = float('inf')
        retArr = []
        
        for key in hashmap2:
            if hashmap2[key] < minIndSum:
                retArr = [key]
                minIndSum = hashmap2[key]
            elif hashmap2[key] == minIndSum:
                retArr.append(key)
        
        return retArr