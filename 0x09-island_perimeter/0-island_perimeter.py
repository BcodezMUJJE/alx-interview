#!/usr/bin/python3

"""
Island perimeter computing module.
"""

def island_perimeter(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
            return 0
        grid[x][y] = 0  # Mark as visited
        return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y - 1) + dfs(x, y + 1)

    def count_border(x, y):
        count = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] == 0:
                count += 1
        return count

    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                perimeter += dfs(x, y)
                perimeter -= count_border(x, y)
    return perimeter
