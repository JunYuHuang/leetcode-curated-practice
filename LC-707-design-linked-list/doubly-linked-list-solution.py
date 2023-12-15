# doubly linked list solution (NeetCode's modded)
class Node:
    def __init__(self, val = -1):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if index == 0 and curr and curr != self.right:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        prev = self.left
        nxt = self.left.next
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if index != 0 or not curr:
            return
        node = Node(val)
        prev = curr.prev
        nxt = curr
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if index != 0 or not curr or curr == self.right:
            return
        prev = curr.prev
        nxt = curr.next
        prev.next = nxt
        nxt.prev = prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
