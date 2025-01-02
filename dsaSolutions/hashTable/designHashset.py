'''
https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/
'''
class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]
    
    def add(self, key: int) -> None:
        ind = key % self.size
        bucketArr = self.buckets[ind]
        for i in bucketArr:
            if i == key:
                return

        self.buckets[ind].append(key)

    def remove(self, key: int) -> None:
        ind = key % self.size
        bucketArr = self.buckets[ind]
        for i in bucketArr:
            if i == key:
                bucketArr.remove(key)

    def contains(self, key: int) -> bool:
        ind = key % self.size
        bucketArr = self.buckets[ind]
        for i in bucketArr:
            if i == key:
                return True
        
        return False
