class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(0), ListNode(0)
        ltail, rtail = left, right
        
        while head:
            if x > head.val:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            
            head = head.next
        
        rtail.next = None
        ltail.next = right.next
        return left.next
        