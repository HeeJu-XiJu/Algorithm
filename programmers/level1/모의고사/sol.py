def solution(answers):
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 1, 2, 3, 2, 4, 2, 5]
    list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer1 = 0
    answer2 = 0
    answer3 = 0
    for i in range(len(answers)):
        if list1[i % len(list1)] == answers[i]:
            answer1 += 1
        if list2[i % len(list2)] == answers[i]:
            answer2 += 1
        if list3[i % len(list3)] == answers[i]:
            answer3 += 1
    
    answer = []
    if answer1 == max(answer1, answer2, answer3):
        answer.append(1)
    if answer2 == max(answer1, answer2, answer3):
        answer.append(2)
    if answer3 == max(answer1, answer2, answer3):
        answer.append(3)
    return answer

print(solution([1, 2, 3, 4, 5]))