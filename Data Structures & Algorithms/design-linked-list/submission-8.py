class ListNode:
    def __init__(
        self,
        val=0,
        next=None,
    ):
        self.val: int = val
        self.next: ListNode | None = next


class MyLinkedList:
    def __init__(self):
        self.head: ListNode | None = None
        self.tail: ListNode | None = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.head

        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        item = ListNode(val=val, next=self.head)
        if self.length == 0:
            self.head = item
            self.tail = item
            self.length += 1
            return

        if self.length == 1:
            self.tail = self.head

        self.head = item

        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.addAtHead(val)
            return

        item = ListNode(val=val, next=None)
        self.tail.next = item
        self.tail = item
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        elif index == self.length:
            self.addAtTail(val)
            return

        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        item = ListNode(val=val, next=curr.next)

        curr.next = item
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return

        curr = self.head

        for _ in range(index - 1):
            curr = curr.next

        curr.next = curr.next.next or None

        if index == self.length - 1:
            self.tail = curr

        self.length -= 1