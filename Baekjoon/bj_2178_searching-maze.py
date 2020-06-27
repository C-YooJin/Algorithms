""" 백준 온라인저지 2178번 미로탐색 """
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    matrix = [[0]*m for _ in range(n)]
    for x in range(n):
        temp = sys.stdin.readline()
        for y in range(m):
            matrix[x][y] = int(temp[y])

    visit = [[0] * m for _ in range(n)]
    queue = [(0, 0)]
    visit[0][0] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        a, b = queue.pop(0)
        if a == n-1 and b == m-1:
            print(visit[n-1][m-1])
            return

        for i in range(4):
            ax = a + dx[i]
            ay = b + dy[i]
            if ax >= 0 and ax < n and ay >= 0 and ay < m:
                if matrix[ax][ay] == 1 and visit[ax][ay] == 0:
                    visit[ax][ay] = (visit[a][b] + 1)
                    matrix[ax][ay] = 0
                    queue.append((ax, ay))

if __name__ == '__main__':
    main()
