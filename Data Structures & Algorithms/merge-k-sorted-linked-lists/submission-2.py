# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap=[]
        for i,lst in enumerate(lists):
            if lst:
                heapq.heappush(minheap,(lst.val,i,lst))
        #pushed all first val in minheap; pop the smallest and push its next
        dummy=ListNode()
        curr=dummy
        while minheap:
            val,i,node=heapq.heappop(minheap)
            curr.next=ListNode(val)
            if node.next:
                node=node.next

                heapq.heappush(minheap,(node.val,i,node))
            curr=curr.next
        
        return dummy.next
        