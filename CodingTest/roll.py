def solution(A, F, M):
    roll = len(A) + F
    total_sum = M * roll

    a_sum = 0
    for i in A:
        a_sum += i

    b = total_sum - a_sum
    tmp_lst = [0]*F

    if b < len(tmp_lst):
        return [0]

    while b > 0:
        for i in range(len(tmp_lst)):
            tmp_lst[i] += 1
            b -= 1
            if tmp_lst[i] > 6:
                return [0]
            if b == 0: break

    return tmp_lst

print(solution([3,2,4,3], 2, 4))
# [6, 6]

print(solution([1,5,6], 4, 3))
# [3, 2, 2, 2] Anyway, 4개의 element의 합이 9가 되면 정답

print(solution([1, 2, 3, 4], 4, 6))
# [0]