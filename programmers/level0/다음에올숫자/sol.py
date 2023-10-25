def solution(common):
    # 등차수열일 때
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1] + (common[1] - common[0])

    # 등비수열일 때
    elif common[1] / common[0] == common[2] / common[1]:
        answer = common[-1] * (common[1] / common[0])
    return answer

print(solution([2, 4, 8]))