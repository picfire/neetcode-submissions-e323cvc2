class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        while (left < right):
            m = left + (right - left) // 2
            if m > 0 and nums[m] < nums[m-1]:
                return nums[m]
            elif nums[left] <= nums[m] and nums[m] > nums[right]:
                left = m +1
            else:
                right = m -1 



        return nums[left]
