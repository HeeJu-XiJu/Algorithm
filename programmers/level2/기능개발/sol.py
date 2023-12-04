def solution(progresses, speeds):
    answer = []
    term = []
    for idx in range(len(progresses)-1, -1, -1):
        if (100 - progresses[idx]) % speeds[idx] == 0 :
            term.append((100 - progresses[idx]) // speeds[idx])
        else:
            term.append((100 - progresses[idx]) // speeds[idx] + 1)

    while len(term) > 0:
        rev = term[-1]
        count = 0
        while len(term) > 0 and term[-1] <= rev:
            term.pop()
            count += 1
        answer.append(count)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))