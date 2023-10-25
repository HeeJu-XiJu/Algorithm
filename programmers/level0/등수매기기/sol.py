def solution(score):
    answer_list = []
    answer = []
    for i in score:
        answer_list.append(sum(i) / 2)

    sort_list = sorted(answer_list, reverse=True)
    
    for i in answer_list:
        answer.append(sort_list.index(i)+1)
    return answer

print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]))