class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([(0, 0, 1)])
        visit = set((0,0))
        directions = [(0,1), (1,0), (0,-1), (-1,0),(-1,1), (1,1), (1,-1), (-1,-1)]

        while queue:
            r, c, length = queue.popleft()

            if min(r,c) < 0 or max(r,c) >= len(grid) or grid[r][c] == 1:
                continue
            if r == c == len(grid) - 1:
                return length
            
            for dr,dc in directions:
                if (r+dr, c+dc) not in visit:
                    queue.append((r+dr, c+dc, length+1))
                    visit.add((r+dr, c+dc))
        return -1

