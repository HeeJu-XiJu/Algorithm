def solution(chicken):
    if chicken <= 10:
        answer = 1
    else :
        answer = (chicken-10) // 9
    return answer

print(solution(1081))