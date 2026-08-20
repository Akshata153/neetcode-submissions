# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        valList=[]
        for lst in lists:
            while lst:
                valList.append(lst.val)
                lst=lst.next
        valList.sort()

        dummy=ListNode()
        curr=dummy
        for n in valList:
            curr.next=ListNode(n)
            curr=curr.next
        return dummy.next


        