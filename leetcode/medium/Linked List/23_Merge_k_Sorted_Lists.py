class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case 1
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if len(lists) > (i + 1) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]
                
    
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