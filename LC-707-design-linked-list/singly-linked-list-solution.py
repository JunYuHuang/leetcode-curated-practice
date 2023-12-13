# My singly linked list solution
class Node:
    def __init__(self, val = -1):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummyHead = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        i = 0
        curr = self.dummyHead.next
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        oldHead = self.dummyHead.next
        newHead = Node(val)
        self.dummyHead.next = newHead
        newHead.next = oldHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.dummyHead
        while curr and curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        i = 0
        prev = self.dummyHead
        curr = prev.next
        newNode = Node(val)
        while curr:
            if i == index: break
            i += 1
            prev = curr
            curr = curr.next
        if prev:
            prev.next = newNode
        newNode.next = curr
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        i = 0
        prev = self.dummyHead
        curr = prev.next
        while curr:
            if i == index: break
            i += 1
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
