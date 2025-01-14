'''
https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/
'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.dataArr = [None] * k
        self.startInd = None
        self.endInd = None
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.length == 0:
            self.startInd = 0
            self.endInd = 0
            self.dataArr[self.endInd] = value
            self.length = 1
            return True
        
        if self.length == len(self.dataArr):
            return False
        
        self.endInd = (self.endInd + 1) % len(self.dataArr)
        self.dataArr[self.endInd] = value
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        
        if self.length == 1:
            self.dataArr[self.startInd] = None
            self.startInd = self.endInd = None
            self.length -= 1
            return True
        
        self.dataArr[self.startInd] = None
        self.startInd = (self.startInd + 1) % len(self.dataArr)
        self.length -= 1
        return True

    def Front(self) -> int:
        if self.startInd == None:
            return -1
        
        return self.dataArr[self.startInd]

    def Rear(self) -> int:
        if self.endInd == None:
            return -1
        
        return self.dataArr[self.endInd]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        if self.length == len(self.dataArr):
            return True
        else:
            return False