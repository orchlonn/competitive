class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case #1
        if head.next == None:
            return head.next

        dummy = ListNode(0, head)
        slow, fast = dummy, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == None or fast.next == None:
                slow.next = slow.next.next
            
        return dummy.next

