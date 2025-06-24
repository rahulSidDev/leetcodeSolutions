'''
https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i, ele in enumerate(citations):
            if n - i <= ele:
                return n-i
        
        return 0
