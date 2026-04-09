class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        for vitri, so in enumerate(nums):
            sodu = target - so

            if sodu in d:
                return [d[sodu],vitri]

            d[so] = vitri

        #target = 7

        