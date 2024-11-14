from collections import deque

n = int(input())

grid = []
for i in range(n):
    grid.append(list(input()))
    
#grid = [['R','R','R','B','B'],['G','G','B','B','B'],['B','B','B','R','R'],['B','B','R','R','R'],['R','R','R','R','R']]

visited = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

# 정상인의 구역수 구하기
def bfs(grid,visited, x,y):
    visited[x][y] = True
    queue = deque([(x,y)])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        cur_x, cur_y = queue.popleft()
        
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if 0 <= next_x < n and 0 <= next_y < n:
                if grid[cur_x][cur_y] == grid[next_x][next_y] and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
    
    return 1

# 적록색약인 사람의 구역 수 구하기
def bfs2(grid, visited, x,y):
    queue2 = deque([(x,y)])
    visited2[x][y] = True
    
    dx2 = [-1,1,0,0]
    dy2 = [0,0,-1,1]
    
    while queue2:
        cur_x2, cur_y2 = queue2.popleft()
        
        for i in range(4):
            next_x2 = cur_x2 + dx2[i]
            next_y2 = cur_y2 + dy2[i]
            
            if 0 <= next_x2 < n and 0 <= next_y2 < n:
                if grid[cur_x2][cur_y2] == grid[next_x2][next_y2] and not visited2[next_x2][next_y2]:
                    visited[next_x2][next_y2] = True
                    queue2.append((next_x2, next_y2))
                elif ((grid[cur_x2][cur_y2] == 'R' and grid[next_x2][next_y2] == 'G') or (grid[cur_x2][cur_y2] == 'G' and grid[next_x2][next_y2] == 'R')) and not visited2[next_x2][next_y2]:
                    visited2[next_x2][next_y2] = True
                    queue2.append((next_x2, next_y2))
    
    return 1
            
normalCnt = 0
weirdCnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            #color = grid[i][j]
            normalCnt+= bfs(grid,visited, i,j)

for i2 in range(n):
    for j2 in range(n):
        if not visited2[i2][j2]:
            #color = grid[i][j]
            weirdCnt+= bfs2(grid,visited2, i2,j2)      
print(normalCnt, weirdCnt)
#print(weirdCnt)
    