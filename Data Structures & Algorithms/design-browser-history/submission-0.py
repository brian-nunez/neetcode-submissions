class ListNode():
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        item = ListNode(val=homepage, next=None, prev=None)
        self.head = item
        self.current = item
        print(f"Init with {item.val}")
        

    def visit(self, url: str) -> None:
        item = ListNode(val=url, next=None, prev=self.current)
        self.current.next = item
        self.current = item
        print(f"Visit {item.val}")
        

    def back(self, steps: int) -> str:
        print(f"Moving back {steps}, current is {self.current.val}")
        curr = self.current
        i = 0
        while curr.prev and i < steps:
            curr = curr.prev
            i += 1
        
        self.current = curr

        return curr.val
        

    def forward(self, steps: int) -> str:
        print(f"Moving forward {steps}, current is {self.current.val}")
        curr = self.current
        i = 0
        while curr.next and i < steps:
            curr = curr.next
            i += 1

        self.current = curr
        return curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)