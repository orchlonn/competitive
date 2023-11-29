class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nextGroupExists, left = True, dummy
        
        while head:
            prev = None
            
            for _ in range(k - 1):
                if head:
                    temp = head.next
                    head.next = prev
                    prev = head
                    head = temp
                else: 
                    nextGroupExists = False
                
            undo = None
            if nextGroupExists != True:
                for _ in range(k - 1):
                    if prev:
                        temp = prev.next
                        prev.next = undo
                        undo = prev
                        prev = temp

            if nextGroupExists == True:
                left.next = prev
            else:
                left.next = undo

            for _ in range(k):
                if left and left.next:
                    left = left.next

            left.next = head
            
        return dummy.next