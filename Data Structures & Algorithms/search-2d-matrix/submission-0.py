class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            for num in row:
                arr.append(num)
        
        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = low + ((high - low) // 2)

            if arr[mid] == target:
                return True
            if arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False