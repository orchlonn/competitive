class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev =  None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        left = dummy
        left = left.next

        while prev and prev.next:
            temp = left.next
            left.next = prev
            prev = prev.next
            left = left.next
            left = temp
            left = left.next
        
        return dummy.next
        