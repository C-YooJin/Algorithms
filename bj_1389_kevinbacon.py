import sys

n, m = map(int, sys.stdin.readline().split())

matrix = [[0] * (n+1) for _ in range(n+1)]

# 인접행렬 생성
for _ in range(1, n+1):
    a, b = map(int, sys.stdin.readline().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

print(matrix)