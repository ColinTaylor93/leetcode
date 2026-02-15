class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create a hashset for storing nums
        found_nums = set()

        # loop through each num, add if not found, remove if in set
        for num in nums:
            if num not in found_nums:
                found_nums.add(num)
            else:
                found_nums.remove(num)
        
        # only 1 should be left and that's our number
        return found_nums.pop()