"""
1. len(s)만큼 돌리면서 i값을 뽑아낸다. 음.. 일단 1개씩 자르는 것 부터 len(s)개 자르는 경우까지 다 해봐야 되기 때문이다.
2. range(len(s)) for문 안에서 일어나는 작업
    - i만큼 자르면서 temp list에 넣는다.
        - i가 1이면 lst[0:1] lst[1:2]
        - i가 2면 lst[0:2] lst[2:4] lst[4:6]
        - i가 3이면 lst[0:3] lst[3:6] lst[6:9]
    - list안에서 for문 돌면서 if lst[j] == lst[j+1]이면 zip_count를 하나 늘려준다. zip_count는 압축된 문자열 갯수 그거..
    - 만약 lst[j] != lst[j+1]이면 new_s에 zip_count랑 lst[j]값을 붙여서 append(string도 append인?) 해준다
        - 여기서 만약 zip_count가 1이면 1 없이 문자열만 붙여준다. (조건문 추가)
    - lst[j]랑 lst[j+1]을 비교하면서 앞에서 해 준 작업을 계속 한다..
    - 결과물을 result_list에 저장한다. 다시 2번으로 돌아가서 2개씩 잘라서 temp에 넣고 반복..
3. result_list에 들어있는 string중 가장 짧은 갯수를 return
"""

def solution(s):
    minA = len(s)
    length = int(len(s)/2)
    for i in range(1, length+1):
        temp_lst = []
        tempStr = ""
        for j in range(0, len(s), i):
            temp_lst.append(s[j:j+i])
        zip_count = 1
        cur_words = temp_lst[0]
        for words in temp_lst[1:]:
            if (cur_words == words):
                zip_count += 1
            else:
                if (zip_count != 1):
                    tempStr += str(zip_count) + cur_words
                else:
                    tempStr += cur_words
                cur_words = words
                zip_count = 1
        if (zip_count != 1):
            tempStr += str(zip_count) + cur_words
        else:
            tempStr += cur_words
        if minA > len(tempStr):
            minA = len(tempStr)
    return minA




    answer = []
    return answer

print(solution('ababcc'))