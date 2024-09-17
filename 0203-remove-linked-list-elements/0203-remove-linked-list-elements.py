# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head =  ListNode(-1)
        prev = dummy_head
        curr = head

        while curr:
            if curr.val != val:
                prev.next = curr
                prev = prev.next
                curr = curr.next
            else:
                curr = curr.next
        prev.next = None
        return dummy_head.next