# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = ''
        number2 = ''
        curr = l1
        while curr:
            number1 += str(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            number2 += str(curr.val)
            curr = curr.next

        number = str(int(number1) + int(number2))
        curr = head = ListNode()
        for i, n in enumerate(number):
            curr.val = int(n)
            if i < len(number)-1:
                curr.next = ListNode()
            curr = curr.next
        
        return head