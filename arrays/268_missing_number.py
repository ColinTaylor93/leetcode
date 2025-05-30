class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # get the max number that should be in tnums
        max_num = len(nums) + 1

        # make nums into a set since lookup is O(1) time
        found_nums = set(nums)

        # loop through the numbers until we find the missing one
        for x in range(max_num):
            if x not in found_nums:
                return x

        # incase all fails return -1
        return -1