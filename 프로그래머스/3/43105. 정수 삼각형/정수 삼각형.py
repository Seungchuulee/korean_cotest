def solution(triangle):
    
    memo = [[-1] * len(row) for row in triangle]
    return dfs(triangle, 0, 0, memo)

def dfs(triangle, i, j, memo):
    
    if i == len(triangle) - 1:
        return triangle[i][j]
    
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    
    left_path = dfs(triangle, i + 1, j, memo)
    right_path = dfs(triangle, i + 1, j + 1, memo)
    
    
    memo[i][j] = triangle[i][j] + max(left_path, right_path)
    
    return memo[i][j]
