class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur:
            nxt = cur.next
            
            if cur.val == val:
                prev.next = nxt
            else:
                prev = cur

            cur = next

        return dummy.next
