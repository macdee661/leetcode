# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        prev = dummy_head
        curr = head
        nums = set(nums)

        while curr:
            if curr.val not in nums:
                prev.next = curr
                prev = prev.next
                curr = curr.next
            else:
                curr = curr.next
        prev.next = None
        return dummy_head.next


        