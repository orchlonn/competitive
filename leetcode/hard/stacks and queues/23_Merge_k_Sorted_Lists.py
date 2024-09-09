# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case
        if len(lists) == 0 or not lists:
            return None
        res = []

        for i in lists:
            res = self.mergeTwoLists(res, i)

        return res


    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l2.val > l1.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next
        
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        
        return dummy.next
