'''
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1018/
'''
class KthLargest:
	# store the input array and the integer 'k'. heapify the stored array so that the largest element is ready
	# at index 0. then continuously remove the top element from the array until only 'k' elements are left.
	# this will cause the 'kth' largest element to always be at the index 0 of the array.
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
    	# if the no. of elements is less than value 'k' then simply heappush the input value onto the array.
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        # otherwise if the input value is greater than the top value of the array then remove the top element
        # from the array and heappush the input value onto the array.
        elif val > self.pool[0]:
            heapq.heappop(self.pool)
            heapq.heappush(self.pool, val)
        
        # return the top element of the heap which is the 'kth' largest element in the array.
        return self.pool[0]