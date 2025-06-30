# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        cur = head
        while slow and slow.next:
            if slow == cur:
                return slow
            slow = slow.next
            cur = cur.next
        
        return None

# Time complexity: O(N)
# Space complexity: O(1)