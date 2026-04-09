class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = (rows * cols) - 1

        # high = 11
        #
        while low <= high:
            # mid = 0 + (11 - 0) // 2 = 5 dư 1
            # how do you get to index 11 or [2][3]
            # 
            mid = low + (high - low) // 2
            row = mid // cols
            col = mid % cols
            

            currentNum = matrix[row][col]
            #print('checking row',row,'and col',col, 'with nums', currentNum)
            if currentNum == target:
                return True

            if currentNum > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

            

        # 1 2 4 8
        # 10 11 12 13
        # 14 20 30 40

        # 1 2 4 8 10 11 12 13 14 20 30 40
