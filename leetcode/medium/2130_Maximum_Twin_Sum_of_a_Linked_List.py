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
    
    
      