# method-dependent doubly linked list solution
class Node:
    def __init__(self, val = ""):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        home = Node(homepage)
        self.curr = home
        self.left = Node()
        self.right = Node()
        self.left.next = home
        self.right.prev = home
        home.prev = self.left
        home.next = self.right

    def visit(self, url: str) -> None:
        page = Node(url)
        prev = self.curr
        nxt = self.right
        prev.next = page
        nxt.prev = page
        page.prev = prev
        page.next = nxt
        self.curr = page

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr and self.curr.prev != self.left:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr and self.curr.next != self.right:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
