def solution(priorities, location):
    q = [0]*len(priorities)
    q[location] = 1
    max_num = max(priorities)

    for _ in range(len(priorities)):
        if priorities[0] != max_num:
            temp = q.pop(0)
            q.append(temp)
            temp_pri = priorities.pop(0)
            priorities.append(temp_pri)
        else:
            return (q.index(1) + 1)

print(solution([1, 1, 9, 1, 1, 1], 0))