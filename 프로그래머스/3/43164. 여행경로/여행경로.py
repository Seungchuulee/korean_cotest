def solution(tickets):
    # 항공권을 사전순으로 정렬
    tickets.sort(reverse=True)  # 사전순으로 정렬하기 위해 역순으로 정렬
    
    routes = {}
    for start, end in tickets:
        if start in routes:
            routes[start].append(end)
        else:
            routes[start] = [end]
    
    # DFS 탐색을 위한 스택
    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]
        # 더 이상 갈 곳이 없으면 경로에 추가
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            # 갈 곳이 남아있으면 스택에 추가
            stack.append(routes[top].pop())
    
    # 경로를 뒤집어서 반환
    return path[::-1]
