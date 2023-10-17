def solution(my_string):
    answer = []
    for i in my_string:
        try:
            if type(int(i)) == int:
                answer.append(int(i))
        except:
            pass
    answer = sorted(answer)
    return answer

print(solution("hi12392"))