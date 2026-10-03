class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        costs = [0] * len(grid[0])

        for row_index, row in enumerate(grid):
            for column_index, value in enumerate(row):
                if row_index == 0 and column_index == 0:
                    costs[column_index] = value
                elif row_index == 0:
                    costs[column_index] = costs[column_index - 1] + value
                elif column_index == 0:
                    costs[column_index] += value
                else:
                    costs[column_index] = (
                        min(costs[column_index], costs[column_index - 1]) + value
                    )

        return costs[-1]
