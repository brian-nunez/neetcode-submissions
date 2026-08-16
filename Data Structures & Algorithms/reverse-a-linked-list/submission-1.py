class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        curr = head

        while curr:
            next = curr.next
            curr.next = previous
            previous = curr
            curr = next

        return previous
