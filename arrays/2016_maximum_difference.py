class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = nums[-1]
        max_difference = -1

        for i, num in enumerate(reversed(nums[:-1])):
            current_index = len(nums) - 2 - i
            if num < max_value:
                difference = max_value - num
                max_difference = max(max_difference, difference)

            max_value = max(max_value, num)
        
        return max_difference