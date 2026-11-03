class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        total = 0
        for num in nums:
            total += max_num - num
        return total
