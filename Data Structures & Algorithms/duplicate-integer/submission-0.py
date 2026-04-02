class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        j, k = 0, 1

        for j in range (len(nums)):
            for k in range(j+1, len(nums)):
                if nums[j] == nums[k]:
                    return True
                
        return False
            
        
