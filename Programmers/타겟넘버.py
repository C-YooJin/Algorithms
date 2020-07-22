# 1. dfs, bfs
# 2. 주어진 numbers로 만들 수 있는 모든 조합의 숫자를 list에 넣는다.
# 3. 그 중 target을 count한다.

def solution(numbers, target):
    super = [0] # super node
    for i in numbers:
        sub = []
        for j in super:
            sub.append(j+i)
            sub.append(j-i)
        super = sub
    return super.count(target)
