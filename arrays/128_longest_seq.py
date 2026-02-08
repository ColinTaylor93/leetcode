class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        nums = set(nums) # removes duplicates
        currentLongest = 0
        for num in nums:
            if num-1 not in nums: # searching a set should be O(1) since it uses a hashtable
                thisNum = 1
                while num + 1 in nums:
                    thisNum += 1
                    num += 1
                currentLongest = max(currentLongest, thisNum)
        return currentLongest