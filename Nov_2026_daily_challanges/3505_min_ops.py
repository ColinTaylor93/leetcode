import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        min_ops = [float('inf')] * (n - x + 1)
        
        # Two-Heap setup for sliding window median:
        max_heap = []
        min_heap = []
        sum_max = 0
        sum_min = 0
        size_max = 0
        size_min = 0
        
        L1 = (x + 1) // 2
        L2 = x - L1
        
        delayed_max = {}
        delayed_min = {}
        
        def clean_tops():
            """Removes stale elements from the top of the heaps (lazy deletion)."""
            while max_heap and -max_heap[0] in delayed_max:
                val = -max_heap[0]
                delayed_max[val] -= 1
                if delayed_max[val] == 0:
                    del delayed_max[val]
                heapq.heappop(max_heap)
            while min_heap and min_heap[0] in delayed_min:
                val = min_heap[0]
                delayed_min[val] -= 1
                if delayed_min[val] == 0:
                    del delayed_min[val]
                heapq.heappop(min_heap)

        def balance():
            """Balances sizes and sums between the two heaps dynamically."""
            nonlocal sum_max, sum_min, size_max, size_min
            clean_tops()
            
            curr_size = size_max + size_min
            if curr_size == 0:
                return
            target_left = (curr_size + 1) // 2
            
            while size_max < target_left and min_heap:
                val = min_heap[0]
                heapq.heappop(min_heap)
                if val in delayed_min:
                    delayed_min[val] -= 1
                    if delayed_min[val] == 0: del delayed_min[val]
                    size_min -= 1
                    clean_tops()
                    continue
                sum_min -= val
                size_min -= 1
                
                heapq.heappush(max_heap, -val)
                sum_max += val
                size_max += 1
                clean_tops()
                
            while size_max > target_left and max_heap:
                val = -max_heap[0]
                heapq.heappop(max_heap)
                if val in delayed_max:
                    delayed_max[val] -= 1
                    if delayed_max[val] == 0: del delayed_max[val]
                    size_max -= 1
                    clean_tops()
                    continue
                sum_max -= val
                size_max -= 1
                
                heapq.heappush(min_heap, val)
                sum_min += val
                size_min += 1
                clean_tops()
                
            clean_tops()

        # Step 1: Slide the window across nums to precompute window uniform costs
        for i in range(n):
            val = nums[i]
            if not max_heap or val <= -max_heap[0]:
                heapq.heappush(max_heap, -val)
                sum_max += val
                size_max += 1
            else:
                heapq.heappush(min_heap, val)
                sum_min += val
                size_min += 1
            balance()
            
            if i >= x:
                out_val = nums[i - x]
                if max_heap and out_val <= -max_heap[0]:
                    delayed_max[out_val] = delayed_max.get(out_val, 0) + 1
                    sum_max -= out_val
                    size_max -= 1
                else:
                    delayed_min[out_val] = delayed_min.get(out_val, 0) + 1
                    sum_min -= out_val
                    size_min -= 1
                balance()
                
            if i >= x - 1:
                median = -max_heap[0]
                cost = (median * L1 - sum_max) + (sum_min - median * L2)
                min_ops[i - x + 1] = cost

        # Step 2: Iterative Bottom-Up DP to pick k non-overlapping windows
        dp = [[float('inf')] * (k + 1) for _ in range(n + 2)]
        for i in range(n + 2):
            dp[i][0] = 0
            
        for count in range(1, k + 1):
            for i in range(n - x * count, -1, -1):
                res = dp[i + 1][count]
                if i <= n - x:
                    take = min_ops[i] + dp[i + x][count - 1]
                    if take < res:
                        res = take
                dp[i][count] = res
                
        return dp[0][k]