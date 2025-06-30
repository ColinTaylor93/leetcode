class Solution:
    from collections import Counter

    def findLHS(self, nums: List[int]) -> int:
        # create a map for the count of each number
        number_counter_map = Counter(nums)

        # find the 2 highest concurrent numbers
        current_max = 0
        for x in number_counter_map:
            if x + 1 in number_counter_map:
                total = number_counter_map[x] + number_counter_map[x+1]
                current_max = max(current_max, total)

        return current_max