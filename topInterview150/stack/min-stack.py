'''
https://leetcode.com/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150
'''
class MinStack:

    def __init__(self):
        self.dataArr = []
        self.length = 0

    def push(self, val: int) -> None:
        self.dataArr.append(val)
        self.length += 1

    def pop(self) -> None:
        if self.length > 0:
            self.dataArr = self.dataArr[:self.length - 1]
            self.length -= 1

    def top(self) -> int:
        return self.dataArr[self.length - 1]

    def getMin(self) -> int:
        minEle = float('inf')
        for ele in self.dataArr:
            if ele < minEle:
                minEle = ele
        
        return minEle


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
