# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = {}
        dummy_head = ListNode(-1)
        prev = dummy_head
        curr = head

        p1 = head
        while p1:
            vals[p1.val] = vals.get(p1.val, 0)+1
            p1 = p1.next
        print(vals)

        while curr:
            if vals[curr.val] > 1:
                curr = curr.next
            else:
                prev.next = curr
                curr = curr.next
                prev = prev.next
        prev.next = None
        return dummy_head.next
            
        