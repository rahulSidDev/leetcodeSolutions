'''
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1386/
'''
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.stack2 = self.invertList(self.stack1)

    def pop(self) -> int:
        retEle = self.stack2.pop()
        self.stack1 = self.invertList(self.stack2)
        return retEle

    def peek(self) -> int:
        return self.stack2[len(self.stack2)-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0
        
    def invertList(self, a: list[int]):
        retList = []
        
        for i in range(len(a)-1, -1, -1):
            retList.append(a[i])
        
        return retList