'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1013/
'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # if the input array is empty or the indexDiff is negative or the valueDiff is negative
        # then return false because all of these cases are invalid for which there is no possible
        # pair of indices.
        if not nums or indexDiff <= 0 or valueDiff < 0:
            return False

        mn = min(nums)
        diff = valueDiff + 1  # In case that `valueDiff` equals 0.
        bucket = {}

        def getKey(num: int) -> int:
            return (num - mn) // diff

        for i, num in enumerate(nums):
            key = getKey(num)
            if key in bucket:  # the current bucket
                return True
            # the left adjacent bucket
            if key - 1 in bucket and num - bucket[key - 1] <= valueDiff:
                return True
            # the right adjacent bucket
            if key + 1 in bucket and bucket[key + 1] - num <= valueDiff:
                return True
            bucket[key] = num
            if i >= indexDiff:
                del bucket[getKey(nums[i - indexDiff])]

        return False