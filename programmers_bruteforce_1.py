def scoreCounter(answers, x):
    score = 0
    index = 0


    for i in range(len(answers)):
        if len(answers) > len(x):
            index = 0

        if answers[i] == x[index]:
            score += 1
            index += 1
        else:
            index += 1

    return score

def solution(answers):
    answer = []

    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    s1counter = scoreCounter(answers, s1)
    s2counter = scoreCounter(answers, s2)
    s3counter = scoreCounter(answers, s3)

    result = {1:s1counter, 2:s2counter, 3:s3counter}

    for key, value in result.items():
        answer.append(value)
    max_num = max(answer)

    answer = []
    for key, value in result.items():
        if value == max_num:
            answer.append(key)

    return answer


print(solution([1,3,2,4,2]))