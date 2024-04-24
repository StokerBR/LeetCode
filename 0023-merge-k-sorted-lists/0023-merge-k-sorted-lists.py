# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        lists = deque(lists)

        while len(lists) > 1:
            l1 = lists.popleft()
            l2 = lists.popleft()

            lists.appendleft(self.merge_lists(l1, l2))

        return lists[0]

    def merge_lists(self, l1, l2):
        merged = ListNode()
        curr = merged

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1 or l2:
            curr.next = l1 if l1 else l2

        return merged.next