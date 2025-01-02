'''
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1134/
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sumsHM = {}
        tupleCount = 0
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] + nums2[j] in sumsHM:
                    sumsHM[nums1[i] + nums2[j]] += 1
                else:
                    sumsHM[nums1[i] + nums2[j]] = 1
        
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                if (0 - (nums3[k] + nums4[l])) in sumsHM:
                    tupleCount += sumsHM[0 - (nums3[k] + nums4[l])]
        
        return tupleCount