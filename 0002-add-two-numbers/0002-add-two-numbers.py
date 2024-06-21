# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        resHead = ListNode()
        curr = resHead
        while l1 or l2:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            s = l1Val + l2Val + remainder
        
            sStr = str(s)
            remainder = 0 if len(sStr) == 1 else int(sStr[0:-1])

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            curr.val = int(sStr[-1])
            if l1 or l2 or remainder:
                curr.next = ListNode(remainder)
                curr = curr.next

        curr = None
        return resHead