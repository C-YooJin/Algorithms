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
        if matrix[start][search] == 1 and (search not in foot_prints):
            dfs(search, matrix, foot_prints)
    return foot_prints

def bfs(start):
    queue = [start]
    foot_prints = [start]
    while queue:
        current_node = queue.pop(0)
        for search in range(len(matrix[current_node])):
            if matrix[current_node][search]==1 and (search not in foot_prints):
                foot_prints += [search]
                queue += [search]
    return foot_prints

#print(dfs(v, matrix, []))
#print(bfs(v))

for i in dfs(v, matrix, []):
    print(i, end='')

print()
for i in bfs(v):
    print(i, end='')