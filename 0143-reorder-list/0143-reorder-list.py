# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
       
        # reverse second half(right)
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # reorder list
        curr = head
        while curr != prev and prev:
            temp_l, temp_r = curr.next, prev.next

            curr.next = prev
            prev.next = temp_l if prev.next else None            

            curr = temp_l
            prev = temp_r
