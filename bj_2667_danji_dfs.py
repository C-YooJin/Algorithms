import sys

# dfs 함수를 하나 만들고
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# map size
n = int(sys.stdin.readline())
# real map
map = [list(sys.stdin.readline()) for _ in range(n)]



print(n)
print(map)
