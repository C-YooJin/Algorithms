def solution(S):
    # a의 개수가 3의 배수이거나 0인 경우만 필터링
    if S.count('a') == 0:
        return len(list(permutations(S, 3)))

    elif S.count('a') % 3 == 0:
        if S[0] == 'b':
            S = S[1:]
            #print(S)
        tmp = S.count('b')
        return pow(2, tmp)
    return 0



print(solution("babaa"))
print(solution("ababa"))
print(solution("aba"))
print(solution("bbbbb"))