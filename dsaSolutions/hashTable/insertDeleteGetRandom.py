'''
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1141/
'''
import random

class RandomizedSet:

    def __init__(self):
        self.setdata = []
        self.datapos = {}

    def insert(self, val: int) -> bool:
        if val not in self.setdata:
            self.setdata.append(val)
            self.datapos[val] = len(self.setdata) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.setdata:
            valInd = self.datapos[val]
            lastEle = self.setdata[-1]
            self.setdata[valInd] = lastEle
            self.datapos[lastEle] = valInd
            self.setdata.pop()
            self.datapos.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return self.setdata[random.randint(0, len(self.setdata)-1)]