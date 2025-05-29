class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Phase 1: Finding the intersection point of the two runners.
        # Start both pointers at the beginning of the list.
        slow_pointer = fast_pointer = 0
        while True:
            # move the slow_pointer by 1 and the fast_pointer by 2, when they meet its a cycle
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]
            if slow_pointer == fast_pointer:
                break

        # Phase 2: Finding the entrance to the cycle (i.e., the duplicate number)
        # Start a new pointer at the beginning
        slow_pointer2 = 0
        while True:
            # Move both pointers by 1 step
            slow_pointer = nums[slow_pointer]
            slow_pointer2 = nums[slow_pointer2]
            # When they meet, it's the duplicate
            if slow_pointer == slow_pointer2:
                return slow_pointer
