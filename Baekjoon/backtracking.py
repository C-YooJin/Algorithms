n, m = map(int, input().split())  # n까지 m개
check = [0 for _ in range(n + 1)]
result = [0 for _ in range(m)]


def sequence(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    for i in range(1, n + 1):
        if check[i] == 1:
            continue
        result[index] = i
        check[i] = 1
        sequence(index + 1, n, m)
        check[i] = 0  


sequence(0, n, m)