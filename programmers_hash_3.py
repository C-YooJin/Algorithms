from collections import Counter

def solution(clothes):

    temp = []
    for i in range(len(clothes)):
        temp.append(clothes[i][1])
    clo_count = Counter(temp)
    #print(clo_count)

    multivalue = 1

    for key, value in clo_count.items():
        multivalue *= value
    #print(multivalue)

    if len(list(clo_count)) == 1:
        return len(clothes)
    else:
        return len(clothes) + multivalue



print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))