class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        num = int(s, 2)

        if num == 1:
            return 0

        while num != 1:
            steps += 1
            # if odd
            if num % 2 == 1:
                num += 1
            else:
                num = num // 2

        return steps
