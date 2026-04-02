class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        #check if key exists. If so, update value of key. 
        #If not, add key to cache. Update both to be MRU
        if key in self.mp:
            self.remove(self.mp[key])
            newNode = Node(key, value)
            self.mp[key] = newNode
            self.insert(self.mp[key])
        else:
            self.mp[key] = Node(key, value)
            self.insert(self.mp[key])
        
        #if capacity exceeded, remove least recently used key
        if len(self.mp) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.mp[lru.key]

