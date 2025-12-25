class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        total = 0

        for i in range(k):
            current = happiness[i] - i
            if current <= 0:
                break
            total += current

        return total
