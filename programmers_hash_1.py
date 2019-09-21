"프로그래머스 고득점 kit hash 1번"

from collections import Counter

def solution(participant, completion):

    parti = Counter(participant)
    comple = Counter(completion)

    result = parti - comple
    answer = list(result)
    return answer[0]


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))