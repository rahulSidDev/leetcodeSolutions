'''
https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # array to store all merged intervals and return at the end.
        retArr = []
        # sort the input array by passing in a lambda function which will convert each interval element
        # into its leftside value. this will cause the input array to be sorted by the left interval value
        # of each interval.
        intervals.sort(key=lambda x: x[0])
        # initial prev with the first interval in the input array.
        prev = intervals[0]

        # loop from the second element to the end of the array.
        for interval in intervals[1:]:
            # if the right value of prev is greater than or equal to the left value of the current interval
            # then the intervals overlap and prev must be updated.
            if interval[0] <= prev[1]:
                # max of both right values is used to update the right value of prev because the right value of
                # either interval could be larger.
                prev[1] = max(prev[1], interval[1])
                # same with the min value of prev since the left value of either interval could be smaller. 
                prev[0] = min(prev[0], interval[0])
            # if intervals don't overlap then append the current prev interval to the return array and update it
            # with the current interval.
            else:
                retArr.append(prev)
                prev = interval
        
        # add the final prev before the loop termination to the return array.
        retArr.append(prev)
        # return the return array.
        return retArr
