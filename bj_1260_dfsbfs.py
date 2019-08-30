""" 백준 알고리즘 1260번 dfs bfs """
# 정점n 간선m 시작v
n, m, v = map(int, input().split())
# print(n, m, v)

# matrix with '0' only
matrix = [[0]*(n+1) for _ in range(n+1)]

# 인접행렬 생성
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

def dfs(start, matrix, foot_prints):
    foot_prints += [start]
    for search in range(len(matrix[start])):
        if (matrix[start][search]) == 1 and (search not in foot_prints):
            dfs(search, matrix, foot_prints)
    return foot_prints

def bfs():
    pass

print(dfs(v, matrix, []))