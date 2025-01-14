'''
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1387/
'''
class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.queue2 = self.invertQueue(self.queue1)

    def pop(self) -> int:
        retEle = self.queue2.pop(0)
        self.queue1 = self.invertQueue(self.queue2)
        return retEle

    def top(self) -> int:
        return self.queue2[0]

    def empty(self) -> bool:
        return len(self.queue1) == 0
        
    def invertQueue(self, a):
        retList = []
        for i in range(len(a)-1, -1, -1):
            retList.append(a[i])
        
        return retList