def solution(lines):
    answer = []
    realanswer = 0

    # 라인 전부를 비교(겹치는지)
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            start1 = lines[i][0]
            end1 = lines[i][1]
            start2 = lines[j][0]
            end2 = lines[j][1]
            if end1 > start2:
                answer.append([max(start1, start2), min(end1, end2)])

    # 겹치는 부분들 경우의 수
    if len(answer) >= 2:
        for i in answer:
            realanswer += abs(i[1] - i[0])
    elif len(answer) == 1:
        realanswer += answer[0][1] - answer[0][0]
    else:
        realanswer = 0
    
    return realanswer

print(solution([[0, 5], [3, 9], [1, 10]]))