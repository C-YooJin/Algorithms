def solution(N):
    binary = list(bin(N)[2:])
    sum = 0

    for i in binary:
        if i == '1':
            sum += 1
    return sum




print(solution(300))