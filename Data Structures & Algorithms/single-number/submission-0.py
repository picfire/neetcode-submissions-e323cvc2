class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        nset = set()

        for item in nums:
            if item in nset:
                nset.remove(item)
            else:
                nset.add(item)

        return list(nset)[0]