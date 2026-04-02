class Node:
    def __init__(self, key, value):
        self.val = value
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
        self.mp = {}
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
            newNode = Node(key, value)
            self.mp[key] = newNode
            self.insert(self.mp[key])
        else:
            self.mp[key] = Node(key, value)
            self.insert(self.mp[key])
        
        while len(self.mp) > self.capacity:
            keyRemove = self.left.next.key
            self.remove(self.mp[keyRemove])
            del self.mp[keyRemove]

        
