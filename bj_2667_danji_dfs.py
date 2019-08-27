import sys

read = lambda: sys.stdin.readline().strip()
# input map size
n = int(read())
# map
map = [list(map(int, list(read()))) for _ in range(n)]
# list of result
danji = []

def dfs(map, cnt, x, y):
    map[x][y] = 0

    # 상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        n_x = x + dx[i]
        n_y = y + dy[i]

        if n_x >= 0 and n_x < n and n_y >= 0 and n_y < n:
            if map[n_x][n_y] == 1:
                cnt = dfs(map, cnt+1, n_x, n_y)
    return cnt

for x in range(n):
    for y in range(n):
        if map[x][y] == 1:
            danji.append(dfs(map, 1, x, y)) # dfs 함수의 결과물을 저장


print(len(danji))
danji = sorted(danji)
for i in danji:
    print(i)



