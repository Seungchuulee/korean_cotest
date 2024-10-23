from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)  # 세로 크기
    m = len(maps[0])  # 가로 크기
    visited = [[False]*m for _ in range(n)]
    def bfs(x,y):
        visited[x][y] = True
        queue =deque([(x,y)])
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        while queue:
            cur_x, cur_y = queue.popleft()
            
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                
                if 0 <= next_x < n and 0 <= next_y < m:
                    if maps[next_x][next_y] == 1 and not visited[next_x][next_y]:
                        maps[next_x][next_y] = maps[cur_x][cur_y]+1
                        visited[next_x][next_y] = True
                        queue.append((next_x,next_y))
                        
        return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1
    
    return bfs(0,0)