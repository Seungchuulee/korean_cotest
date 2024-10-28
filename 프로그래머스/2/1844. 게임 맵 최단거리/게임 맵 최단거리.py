from collections import deque

def bfs(x, y, maps, visited, n, m):
    visited[x][y] = True
    queue = deque([(x, y)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if 0 <= next_x < n and 0 <= next_y < m:
                if maps[next_x][next_y] == 1 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    maps[next_x][next_y] = maps[cur_x][cur_y] + 1
                    queue.append((next_x, next_y))
    
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1

def solution(maps):
    n = len(maps)  # 행의 개수
    m = len(maps[0])  # 열의 개수
    visited = [[False] * m for _ in range(n)]  # 방문 기록 배열
    
    # BFS를 시작 지점 (0, 0)에서 실행
    return bfs(0, 0, maps, visited, n, m)
