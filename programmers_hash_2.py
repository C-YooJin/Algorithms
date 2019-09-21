"프로그래머스 고득점 kit hash 2"

def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return True
    return False


print(solution(["119", "97674223", "1195524421"]))