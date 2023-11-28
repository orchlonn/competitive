class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy

        while head and head.next:
            if head and head.next and head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                left.next = left.next
            else:
                left = left.next
            
            right = right.next

        return dummy.next