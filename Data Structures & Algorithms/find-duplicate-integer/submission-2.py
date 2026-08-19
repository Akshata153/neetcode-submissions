class Solution:
    def findDuplicate(self, arr: List[int]) -> int:
        fast,slow=0,0

        while True:
            slow=arr[slow]
            fast=arr[arr[fast]]
            if slow==fast:
                break
        slow1=0
        while True:
            slow1=arr[slow1]
            slow=arr[slow]
            if slow1==slow:
                return slow
        return -1