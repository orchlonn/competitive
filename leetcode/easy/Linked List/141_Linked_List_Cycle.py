# Definition for singly-linked list.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slower, faster = head, head

        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next
            if slower == faster:
                return True
        
        return False
        