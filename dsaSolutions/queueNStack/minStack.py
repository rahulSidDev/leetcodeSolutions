'''
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/
'''
class MinStack:

    def __init__(self):
        self.dataArr = []

    def push(self, val: int) -> None:
        self.dataArr.append(val)

    def pop(self) -> None:
        self.dataArr = self.dataArr[:len(self.dataArr)-1]

    def top(self) -> int:
        return self.dataArr[len(self.dataArr)-1]

    def getMin(self) -> int:
        minEle = float('inf')
        for ele in self.dataArr:
            if ele < minEle:
                minEle = ele
        
        return minEle