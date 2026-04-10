
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # return the minimum eating rate or pile size(k)

        # if current_pile <= k: eat it and move on

        # so utilize all of the hours, and minimize the eating rate

        length = len(piles)
        if length == h:
            return max(piles)
        
        result = 0
        # upper bound
        upper = max(piles)
        lower = 1
        result = upper
        while lower <= upper:
            k = lower + (upper - lower) // 2

            total_hours = 0

            for pile in piles:
                total_hours += (pile + k - 1) // k
            if total_hours <= h:
                result = min(result,k)
            
                upper = k - 1
            else:
                lower = k + 1
        return result


        
