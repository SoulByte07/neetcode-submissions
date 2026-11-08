class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        resIslands = 0
        visited = set()

        def bfs(r, c):
            queue = collections.deque()
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr in range(row)) and (nc in range(col)) and ((nr, nc)) not in visited and grid[nr][nc]=='1':
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1' and ((r, c) not in visited):
                    resIslands += 1
                    bfs(r, c)
        return resIslands
            