# method-dependent T and S array and linked list solution (NeetCode's modded)
class ListNode:
    def __init__(self, key = -1):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.store = [ListNode() for i in range(10 ** 4)]
        self.size = len(self.store)

    def keyToHash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        pos = self.keyToHash(key)
        curr = self.store[pos]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        pos = self.keyToHash(key)
        curr = self.store[pos]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        pos = self.keyToHash(key)
        curr = self.store[pos]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
