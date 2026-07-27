class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=len(nums1)+len(nums2)
        half=total//2
        if len(nums2)<len(nums1):
            nums1,nums2=nums2,nums1
        l,r=0,len(nums1)-1
        while True:
            i=(l+r)//2
            j=half-i-2
            Aleft=nums1[i] if i>=0 else float('-inf')
            Aright=nums1[i+1] if (i+1)<len(nums1) else float('inf')
            Bleft=nums2[j] if j>=0 else float('-inf')
            Bright=nums2[j+1] if (j+1)<len(nums2) else float('inf')

            # crt partition
            if Aleft<=Bright and Aright>=Bleft:
                if total%2:
                    #odd, bcz of //2 before in half we have removed one from half hence we choose other half i.e right
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright: #extra element in A half,so move pointer towards left
                r=i-1
            else:
                l=i+1


                
