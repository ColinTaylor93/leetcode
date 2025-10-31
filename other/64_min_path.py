import heapq

class Solution:
    def minPathSum(self, grid):
        """
        Finds the min path sum using Dijkstra's algorithm
        """
        rows, cols = len(grid), len(grid[0])
        priority_queue = [(grid[0][0], 0, 0)]

        # Distance matrix to track the minimum cost to each cell
        min_cost = [[float("inf")] * cols for _ in range(rows)]
        min_cost[0][0] = grid[0][0]

        # Possible moves: down, right
        directions = [(1, 0), (0, 1)]

        while priority_queue:
            cost_so_far, row, col = heapq.heappop(priority_queue)

            # If we reach the bottom-right, return the cost
            if row == rows - 1 and col == cols - 1:
                return cost_so_far

            # If there's already a better path, skip
            if cost_so_far > min_cost[row][col]:
                continue

            for d_row, d_col in directions:
                next_row, next_col = row + d_row, col + d_col

                if 0 <= next_row < rows and 0 <= next_col < cols:
                    new_cost = cost_so_far + grid[next_row][next_col]

                    if new_cost < min_cost[next_row][next_col]:
                        min_cost[next_row][next_col] = new_cost
                        heapq.heappush(priority_queue, (new_cost, next_row, next_col))

        return min_cost[rows - 1][cols - 1]
