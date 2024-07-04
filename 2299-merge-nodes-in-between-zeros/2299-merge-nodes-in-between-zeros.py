# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        currNew = newList
        curr = head.next
        currSum = 0
        while curr:
            if curr.val == 0:
                currNew.val = currSum
                currSum = 0
                if curr.next:
                    currNew.next = ListNode()
                    currNew = currNew.next
            else:
                currSum += curr.val
            curr = curr.next
        return newList