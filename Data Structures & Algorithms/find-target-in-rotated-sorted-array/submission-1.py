class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums == None or len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1

        while left < right:
            m = left + (right - left) // 2
            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m
        
        start = left 
        left = 0
        right = len(nums) - 1

        if target >= nums[start] and target <= nums[right]:
            left = start
        else:
            right = start - 1

        while left <= right:
            m = left + (right - left) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        return -1