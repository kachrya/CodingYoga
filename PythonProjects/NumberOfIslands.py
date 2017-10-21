class Solution(object):
    g = [[]]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.g = grid
        islands = 0
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                islands += self.sink(i, j)
        return islands

    def sink(self, i, j):
        if i < 0 or i == len(self.g) or j < 0 or j == len(self.g[i]) or self.g[i][j] == '0':
            return 0
        """
        if we reach here, [i][j] is 1

                i-1, j
         i,j-1  (i j)    i,j+1
                i+1, j

        """
        self.g[i][j] = '0'
        self.sink(i+1, j)
        self.sink(i-1, j)
        self.sink(i, j+1)
        self.sink(i, j-1)
        return 1

soln = Solution()
grid = [['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']]
print(soln.numIslands(grid))