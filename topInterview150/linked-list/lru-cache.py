'''
https://leetcode.com/problems/lru-cache/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        firstNode = self.head.next
        node.next = firstNode
        node.prev = self.head
        firstNode.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        retNode = self.cache[key]
        self.remove(retNode)
        self.add(retNode)
        return retNode.value

    def remove(self, node):
        nextNode = node.next
        prevNode = node.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            currNode = self.cache[key]
            self.remove(currNode)
            del self.cache[key]
        
        if len(self.cache) >= self.capacity:
            tailNode = self.tail.prev
            self.remove(tailNode)
            del self.cache[tailNode.key]
        
        newNode = Node(key, value)
        self.add(newNode)
        self.cache[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
