# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        dummy = res
        carry = 0
        while l1 or l2 or carry:
            temp = ListNode(0)
            if l1 and l2:
                summ = l1.val + l2.val + carry

            elif l1:
                summ = l1.val + carry
            
            elif l2:
                summ = l2.val + carry

            elif carry > 0:
                summ = carry
            
            if summ > 9:
                carry = 1
                temp.val = summ%10
            else:
                carry = 0
                temp.val = summ
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            res.next = temp
            res = res.next
        
        return dummy.next
            
