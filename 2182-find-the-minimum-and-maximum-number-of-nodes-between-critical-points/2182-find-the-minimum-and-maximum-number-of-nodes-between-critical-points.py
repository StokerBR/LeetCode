# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        i = 1
        first = None
        last = None
        minDistance = float('inf')
        maxDistance = -1
        curr = head

        while curr.next:
            if curr.next.next and (curr.val > curr.next.val < curr.next.next.val or curr.val < curr.next.val > curr.next.next.val):
                if first:
                    maxDistance = max(maxDistance, i-first)
                else:
                    first = i

                if last:
                    minDistance = min(minDistance, i-last)

                last = i

            i += 1
            curr = curr.next

        return [minDistance if minDistance != float('inf') else -1, maxDistance]