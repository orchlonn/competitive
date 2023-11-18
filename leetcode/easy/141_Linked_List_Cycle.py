# Definition for singly-linked list.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slower = head
        faster = head

        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
            if slower == faster:
                return True
            
            
        return False
            
        

