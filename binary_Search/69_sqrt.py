class Solution:
    def mySqrt(self, x: int) -> int:
        # if less then 2 the answer is just x
        if x < 2:
            return x
        
        # Binary search till its right
        left, right = 0, x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                ans = mid 
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
        
