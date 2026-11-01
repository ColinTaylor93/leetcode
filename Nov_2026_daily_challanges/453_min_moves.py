class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # Lowering one element equals raising all others so this is all we need
        return sum(nums) - len(nums) * min(nums)