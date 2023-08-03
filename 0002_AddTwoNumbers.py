# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1 != None:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2 != None:
            num2 = str(l2.val) + num2
            l2 = l2.next
         
        num = int(num1) + int(num2)
        l1 = ListNode(0, None)
        l1.val = num%10
        num //= 10
        l2 = l1
        while num:
            l1.next = ListNode(0, None)
            l1 = l1.next
            l1.val = num%10
            num //= 10
        return l2
        