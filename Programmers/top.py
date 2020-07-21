def solution(heights):
    answer = []
    answer.append(0)

    for i in range(len(heights)):
        check = 0
        if i == 0: continue
        for j in range(i - 1, -1, -1):
            if heights[j] > heights[i]:
                answer.append(j + 1)
                check = 1
                break
        if check == 0: answer.append(0)
    return answer



print(solution([3,9,9,3,5,7,2]))
# [0,0,0,3,3,3,6] 나와야 됨