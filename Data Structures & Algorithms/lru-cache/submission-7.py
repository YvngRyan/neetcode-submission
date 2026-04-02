class ListNode:
    def __init__(self, key=0, value=0, next=None, prev=None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.length = 0

        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    def insert(self, node):
        tmp = self.head.next
        self.head.next = node
        node.next = tmp
        node.prev = self.head
        tmp.prev = node
    
    def remove(self, node):
        next, prev = node.next, node.prev
        next.prev = prev
        prev.next = next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            currNode = self.cache[key]
            currNode.val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            newNode = ListNode(key, value)
            self.cache[key] = newNode
            self.insert(newNode)
            self.length += 1
            if self.length > self.capacity:
                removedNode = self.tail.prev
                self.remove(removedNode)
                self.length -= 1
                del self.cache[removedNode.key]
        
