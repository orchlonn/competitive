class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length, tail = 1, head
        
        while tail and tail.next:
            tail = tail.next
            length += 1
        
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        
        newHead = cur.next
        cur.next = None
        tail.next = head

        return newHead
