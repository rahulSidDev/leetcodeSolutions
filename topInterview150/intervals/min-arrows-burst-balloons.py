'''
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sorts the points array based on the left interval values
        points.sort(key=lambda x: x[0])
        # the no. of max arrow shots to be taken is the length of the points array.
        arrowShots = len(points)
        # initialise the intersection of intervals as null.
        intersection = None

        for i, point in enumerate(points):
            # if index is 0 zero then the current point is the first point. in this case assign the point
            # to the intersection var.
            if i == 0:
                intersection = point
            # if index is not zero then compare the current point with the intersection to see if there is any
            # overlap.
            else:
                # if the right value of intersection is greater than equal to the current point then that means
                # overlapping has occured.
                if intersection[1] >= point[0]:
                    # updated the intersection to be the intersecting common range between the current point and the
                    # previous intersection.
                    intersection = [max(point[0], intersection[0]), min(point[1], intersection[1])]
                    # since an overlap has occured the no. of arrows required will be 1 less than before and so no. of
                    # arrow shots is decremented by 1.
                    arrowShots -= 1
                else:
                    # if there is not overlap then simply assign the current point to the intersection var for the next iter.
                    intersection = point
        
        # return the no. of arrow shots var.
        return arrowShots
