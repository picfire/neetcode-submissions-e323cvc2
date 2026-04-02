class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        nums3 = nums1+nums2
        nums3 = sorted(nums3)
        middle = len(nums3) / 2
        target = math.floor(len(nums3) / 2)




        if len(nums3) % 2 != 0:     
                num = nums3[target]
                return num
        else:
            top = int(middle)
            numt = nums3[top]
            bottom = int(middle -1)
            numb = nums3[bottom]
            tb = (numt + numb) / 2
            return tb


                
