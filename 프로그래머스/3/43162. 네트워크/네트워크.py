def dfs(computers, visited, i):
    # 현재 컴퓨터 i를 방문 처리
    visited[i] = True
    
    # i 컴퓨터와 연결된 다른 컴퓨터들을 확인
    for j in range(len(computers)):
        # computers[i][j]가 1이면, i와 j가 연결된 상태
        if computers[i][j] == 1 and not visited[j]:
            dfs(computers, visited, j)  # 연결된 컴퓨터에 대해 다시 탐색


def solution(n,computers):
    
    visited = [False] * n  # 방문한 컴퓨터 체크용 리스트
    count = 0  # 네트워크 개수를 세는 변수

    # 모든 컴퓨터를 순회하며, 아직 방문하지 않은 컴퓨터 발견 시 DFS 탐색
    for i in range(n):
        if not visited[i]:  # 방문하지 않은 컴퓨터 발견
            dfs(computers, visited, i)  # 그 컴퓨터와 연결된 모든 네트워크를 탐색
            count += 1  # 새로운 네트워크가 발견될 때마다 1 증가

    return count  # 네트워크 개수 반환
