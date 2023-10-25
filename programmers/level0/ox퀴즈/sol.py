def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        quiz_list = quiz[i].split()
        if eval(quiz_list[0] + quiz_list[1] + quiz_list[2]) == int(quiz_list[-1]):
            answer.append("O")
        else :
            answer.append("X")
    return answer

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))