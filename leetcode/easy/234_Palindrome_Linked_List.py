# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case #1
        if head.next == None:
            return True

        # create the pointers
        slow, fast = head, head
        
        # find the 2nd half
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # assign the current value and reverse the 2nd half
        cur = head
        prev = None
        while slow:
            nxtPoint = slow.next
            slow.next = prev
            prev = slow
            slow = nxtPoint
        
        # checks every element from 1st and 2nd half
        while prev:
            if prev.val != cur.val:
                return False
                break
            else:
                prev = prev.next
                cur = cur.next
        
        return True
