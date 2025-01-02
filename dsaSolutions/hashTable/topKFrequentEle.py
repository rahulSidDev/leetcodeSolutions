'''
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1133/
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyHM = {}
        freqArrHM = {}
        resultArr = []
        allKeys = []
        
        for num in nums:
            if num not in frequencyHM:
                frequencyHM[num] = 1
            else:
                frequencyHM[num] += 1
        
        for key in frequencyHM:
            if frequencyHM[key] not in freqArrHM:
                freqArrHM[frequencyHM[key]] = [key]
                allKeys.append(frequencyHM[key])
            else:
                freqArrHM[frequencyHM[key]].append(key)
        
        allKeys.sort()
        allKeys = allKeys[::-1]
        
        for i in range(len(allKeys)):
            resultArr += freqArrHM[allKeys[i]]
        
        return resultArr[:k]