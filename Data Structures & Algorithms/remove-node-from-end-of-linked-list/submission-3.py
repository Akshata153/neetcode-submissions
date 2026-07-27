# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head        
        total=0
        temp=curr
        while temp:
            total+=1
            temp=temp.next
        rem=total-n
        count=0
        if rem==0:
            return head.next
        # print(rem)
        for i in range(rem+1):
            if (i+1)==rem:
                # print(i+1)
                curr.next=curr.next.next
                # print(curr)
                break
            curr=curr.next
        return head
            



