import sys

lst = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

def solution(lst, target):
    if len(lst) == 0 or lst is None:
        return []

    hashtable = {}
    for i, v in enumerate(lst):
        if (target - v) in hashtable:
            print([hashtable[target - v], i])
        hashtable[v] = i

solution(lst, target)