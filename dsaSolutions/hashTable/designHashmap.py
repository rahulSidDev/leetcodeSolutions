'''
https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/
'''
class ListNode:
    def __init__(self, key, value, nxt):
        self.key = key
        self.value = value
        self.next = nxt

class MyHashMap:
    def __init__(self):
        self.size = 19997
        self.mult = 12582917
        self.data = [None for _ in range(self.size)]

    def hashFunc(self, key):
        return key * self.mult % self.size # multiplicative hashing function
    
    def put(self, key: int, value: int) -> None:
        self.remove(key)
        
        ind = self.hashFunc(key)
        newNode = ListNode(key, value, self.data[ind])
        self.data[ind] = newNode

    def get(self, key: int) -> int:
        ind = self.hashFunc(key)
        node = self.data[ind]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        
        return -1

    def remove(self, key: int) -> None:
        ind = self.hashFunc(key)
        node = self.data[ind]
        
        if not node:
            return
        
        if node.key == key:
            self.data[ind] = node.next
            return
        
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next