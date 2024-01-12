# O(1) T and O(1) S doubly linked list solution
class Node:
    def __init__(self, key = -2, val = -2):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> node
        self.left = Node() # dummy head points to LRU node
        self.right = Node() # dummy tail points to most recent (MRU) node
        self.left.next = self.right
        self.right.prev = self.left

    # inserts as new tail (MRU)
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
