#!usr/nib/python3
"""
This function returns the perimeter
of an island described in grid
"""


def island_perimeter(grid):
    """
    Args: grid which is a list
          of positive integers
    Returns: An integer, which is the perimeter
          of the island
    """
    # initialize a set to keep track of
    # the spot we've touched
    visit = set()

    """
    this function help us with our boundries
    """

    def dfs(i, j):
        """
        Args: i and j (rows and cols of our grid)
        Returns: The perimeter
        """

        if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        if (i, j) in visit:
            return 0

        visit.add((i, j))

        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i - 1, j)
        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
