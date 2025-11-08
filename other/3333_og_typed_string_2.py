class Solution:
    MOD = 10**9 + 7

    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:
            return 0  # Edge case: not enough characters for any valid original string
        if n == k:
            return 1  # Only one possible original string (no repeated characters)

        # Step 1: Segment word into runs of consecutive same characters
        seg = [1]
        for i in range(1, n):
            if word[i] == word[i - 1]:
                seg[-1] += 1
            else:
                seg.append(1)
        m = len(seg)

        # Step 2: Compute total possible strings (product of all segment lengths)
        total = 1
        take_mod = False
        for length in seg:
            total *= length
            if total >= self.MOD:
                total %= self.MOD
                take_mod = True

        if total == 1 and not take_mod:
            return 1  # Special case: all segments are length 1

        if k <= m:
            return total  # Any valid configuration of at least 1 key per segment is allowed

        # Step 3: Count invalid configurations (original length < k)
        maxT = k - m - 1  # Max extra characters we can avoid typing
        if maxT < 0:
            return total  # All strings are valid

        # Initialize DP arrays
        dp = [[0] * (maxT + 1) for _ in range(2)]
        dp[0][0] = 1  # Base case: zero skipped characters

        for j in range(m):
            s = seg[j] - 1  # max number of characters we can skip in this segment
            prefix = [0] * (maxT + 2)  # 1-indexed prefix sum array
            for i in range(maxT + 1):
                prefix[i + 1] = (prefix[i] + dp[j % 2][i]) % self.MOD
            for i in range(maxT + 1):
                L = max(0, i - s)
                R = i
                dp[(j + 1) % 2][i] = (prefix[R + 1] - prefix[L] + self.MOD) % self.MOD

        # Sum up all invalid configurations (original string shorter than k)
        less_than_k = sum(dp[m % 2]) % self.MOD

        return (total - less_than_k + self.MOD) % self.MOD