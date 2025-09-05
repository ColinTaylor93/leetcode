class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Create an empty n x n matrix
        spiral_matrix = [[0] * n for _ in range(n)]
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0  # Start moving right
        
        # Start position
        row, col = 0, 0  
        
        # Fill the matrix with values from 1 to n^2
        for value in range(1, n * n + 1):
            spiral_matrix[row][col] = value
            
            # Determine the next step in row and column
            row_step, col_step = directions[direction_index]
            next_row, next_col = row + row_step, col + col_step
            
            # Check if next position is valid; if not, turn clockwise
            if (0 <= next_row < n and 0 <= next_col < n 
                    and spiral_matrix[next_row][next_col] == 0):
                row, col = next_row, next_col
            else:
                direction_index = (direction_index + 1) % 4
                row_step, col_step = directions[direction_index]
                row, col = row + row_step, col + col_step
        
        return spiral_matrix