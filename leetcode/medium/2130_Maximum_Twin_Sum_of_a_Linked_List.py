# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: # Solution - 1
    def pairSum(self, head: Optional[ListNode]) -> int:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        
        left, right = 0, len(array) - 1
        res = 0

        while right > left:
            sum = array[right] + array[left]
            if sum > res:
                res = sum

            right -= 1
            left += 1
        
        return res
    
    
class Solution: # Solution - 2
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        res = 0
        while slow and prev:   
            res = max(res, prev.val + slow.val)
            
            slow = slow.next
            prev = prev.next
        
        return res
