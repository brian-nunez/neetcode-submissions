class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        previous = None
        curr = head
        next = head.next

        while curr is not None:
            curr.next = previous
            previous = curr
            curr = next
            if next is not None:
                next = next.next

        return previous
