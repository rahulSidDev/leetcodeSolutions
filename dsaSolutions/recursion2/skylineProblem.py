'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
The geometric information of each building is given in the array 'buildings' where 'buildings[i] = [lefti, righti, heighti]':

1. 'lefti' is the x coordinate of the left edge of the 'ith' building.
2. 'righti' is the x coordinate of the right edge of the 'ith' building.
3. 'heighti' is the height of the 'ith' building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height '0'.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form '[[x1,y1],[x2,y2],...]'. 
Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always 
has a y-coordinate '0' and is used to mark the skyline's termination where the rightmost building ends. Any ground between the 
leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, 
'[...,[2 3],[4 5],[7 5],[11 5],[12 7],...]' is not acceptable; the three lines of height 5 should be merged into one in the final 
output as such: '[...,[2 3],[4 5],[12 7],...]'
'''
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos: heappop(live)
            if negH: heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [ [pos, -live[0][0]] ]
        return res[1:]