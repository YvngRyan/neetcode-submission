class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.capacity = capacity

        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def update(self, node):
        tmp = self.tail.prev
        self.tail.prev = node
        tmp.next = node
        node.next = self.tail
        node.prev = tmp
    
    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev, prev.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.keys:
            self.remove(self.keys[key])
            self.update(self.keys[key])

            return self.keys[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.remove(self.keys[key])
        
        self.keys[key] = ListNode(key, value)
        self.update(self.keys[key])

        if len(self.keys) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.keys[lru.key]