# method dependent array and linked list solution (NeetCode's modded)
class ListNode:
    def __init__(self, key = -1, value = -1):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.store = [ListNode() for i in range(10 ** 4)]
        self.size = len(self.store)

    def keyToHash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        pos = self.keyToHash(key)
        curr = self.store[pos]
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        pos = self.keyToHash(key)
        curr = self.store[pos]
        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        pos = self.keyToHash(key)
        curr = self.store[pos]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
