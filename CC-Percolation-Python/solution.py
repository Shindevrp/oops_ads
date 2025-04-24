def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def dfs(grid, x, y, visited, n):
    stack = [(x, y)]
    visited[x][y] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if is_valid(nx, ny, n) and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))

def percolates(n, open_sites):
    grid = [[0] * n for _ in range(n)]
    for site in open_sites:
        grid[site[0] - 1][site[1] - 1] = 1
    
    visited = [[False] * n for _ in range(n)]
    
    for col in range(n):
        if grid[0][col] == 1 and not visited[0][col]:
            dfs(grid, 0, col, visited, n)
    
    for col in range(n):
        if visited[n - 1][col]:
            return True
    
    return False

n = int(input())
open_sites = []
while True:
    try:
        line = input()
        if not line:
            break
        x, y = map(int, line.split())
        open_sites.append((x, y))
    except EOFError:
        break

if percolates(n, open_sites):
    print("true")
else:
    print("false")