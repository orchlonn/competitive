class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case 1
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergeList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if len(lists) > (i + 1) else None
                mergeList.append(self.mergeTwoLists(l1,l2))
            lists = mergeList
        
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next