'''
https://leetcode.com/problems/insert-interval/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # if the intervals array is empty then return an array with just the new interval inserted.
        if not intervals:
            return [newInterval]
        
        # assign new interval to the meged interval which will be updated when overlapping intervals are
        # encountered in the iteration.
        mergedInts = newInterval
        # return array to store the new intervals.
        retArr = []
        # boolean variable to store whether the new interval has been inserted into the merge array or not.
        intInserted = False
        
        # iterate over the entire intervals array.
        for i, interval in enumerate(intervals):
            # if the merged interval's right value is less than the current interval's left value then that means
            # there are no more overlaps and the current position is where the merged interval must be inserted.
            if mergedInts[1] < interval[0]:
                # updated the return array by adding the mergedInt and the remaining intervals array.
                retArr += [mergedInts] + intervals[i:]
                # mark interval inserted variable as true and break the loop.
                intInserted = True
                break
            # otherwise there might be an overlap with the current interval and the merged interval.
            else:
                # if the left value of merged interval is less than equal to the right value of current interval
                # then that means there is an overlap.
                if mergedInts[0] <= interval[1]:
                    # create the new merged interval by taking the min of both interval's left values and the max of 
                    # the right values of both intervals. update the merged interval with the newly merged interval.
                    mergedInts = [min(interval[0], mergedInts[0]), max(interval[1], mergedInts[1])]
                # otherwise the current interval is not overlapping with the merged interval and it is simply appended to the
                # return array.
                else:
                    retArr.append(interval)
        
        # if the merged interval is not inserted then do so after the loop has ended.
        if not intInserted:
            retArr.append(mergedInts)
        
        # return the return array.
        return retArr
