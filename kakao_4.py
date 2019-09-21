def solution(words, queries):
    answer = []
    for query in queries:
        answer.append(wordCount(query, words))
    return answer

def wordCount(query, wordsList):
    replacedQuery = query.replace('?','');
    count = 0
    start = -1
    end = -1
    for i in range(len(query)):
        if query[i] == '?' and start == -1:
            start = i
            if i == len(query)-1:
                end = i
        elif start != -1 and query[i] != '?':
            end = i-1
            break
        elif end == -1 and i == len(query)-1:
            end = i
    for word in wordsList:
        if len(query) != len(word):
            continue
        else:
            # ? 로 시작하는 경우
            if start == 0:
                if len(word)-1 == end:
                    count += 1
                    continue
                if word[end+1:] == replacedQuery:
                    count += 1
            #? 로 시작 안하는 경우
            else:
                if word[0:start] == replacedQuery:
                    count += 1
    return count
