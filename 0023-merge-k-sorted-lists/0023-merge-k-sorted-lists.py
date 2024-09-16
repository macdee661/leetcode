# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)        

        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        
        head = ListNode()
        p = head

        while heap:
            p.next = ListNode(heapq.heappop(heap))
            p = p.next

        return head.next

