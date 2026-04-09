class Solution:
    def search(self, nums: List[int], target: int) -> int:


        low = 0
        high = len(nums) - 1

        # [-1,0,2,4,6,8]
        #  0  1 2 3 4 5
        #  |          |

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                low = low + 1
            else:
                high = high - 1
        return -1

