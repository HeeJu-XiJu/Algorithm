def solution(hp):
    ant_1 = hp // 5
    ant_1_rest = hp % 5
    ant_2 = ant_1_rest // 3
    ant_3 = ant_1_rest % 3
    answer = ant_1 + ant_2 + ant_3
    return answer

print(solution(999))