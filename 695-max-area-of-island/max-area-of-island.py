class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            area = 1
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit:
                        visit.add((r,c))
                        q.append((r,c))
                        area += 1
            return area

        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = bfs(r,c)
                    max_area = max(area, max_area)
        return max_area        