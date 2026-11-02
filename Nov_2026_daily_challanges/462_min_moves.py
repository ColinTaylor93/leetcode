class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Sort the array to find the median
        nums.sort()

        # The median is at the middle index
        median = nums[len(nums) // 2]

        # Calculate the sum of absolute differences from the median
        return sum(abs(num - median) for num in nums)
