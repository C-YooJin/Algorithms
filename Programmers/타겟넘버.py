def solution(numbers, target):
    super = [0] # super node
    for i in numbers:
        sub = []
        for j in super:
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
    return super.count(target)